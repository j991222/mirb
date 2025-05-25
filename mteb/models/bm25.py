from __future__ import annotations

import logging
from functools import partial

from mteb.evaluation.evaluators.RetrievalEvaluator import DRESModel
from mteb.model_meta import ModelMeta

from .wrapper import Wrapper
import numpy as np

logger = logging.getLogger(__name__)


def bm25_loader(**kwargs):
    try:
        import bm25s
        import Stemmer
    except ImportError:
        raise ImportError(
            "bm25s or PyStemmer is not installed. Please install it with `pip install mteb[bm25s]`."
        )

    class BM25Search(DRESModel, Wrapper):
        """BM25 search"""

        def __init__(
            self,
            previous_results: str = None,
            stopwords: str = "en",
            stemmer_language: str | None = "english",
            **kwargs,
        ):
            super().__init__(
                model=None,
                batch_size=1,
                corpus_chunk_size=1,
                previous_results=previous_results,
                **kwargs,
            )

            self.stopwords = stopwords
            self.stemmer = (
                Stemmer.Stemmer(stemmer_language) if stemmer_language else None
            )


        @classmethod
        def name(self):
            return "bm25s"

        def search(
            self,
            corpus: dict[str, dict[str, str]],
            queries: dict[str, str | list[str]],
            excluded_ids: dict[str, list[str]],
            top_k: int,
            return_sorted: bool = False,
            **kwargs,
        ) -> dict[str, dict[str, float]]:
            logger.info("Encoding Corpus...")
            corpus_ids = list(corpus.keys())
            corpus_with_ids = [
                {
                    "doc_id": cid,
                    **(
                        {"text": corpus[cid]}
                        if isinstance(corpus[cid], str)
                        else corpus[cid]
                    ),
                }
                for cid in corpus_ids
            ]

            corpus_texts = [
                "\n".join([doc.get("title", ""), doc["text"]])
                for doc in corpus_with_ids
            ]  # concatenate all document values (title, text, ...)
            encoded_corpus = self.encode(corpus_texts)

            logger.info(
                f"Indexing Corpus... {len(encoded_corpus.ids):,} documents, {len(encoded_corpus.vocab):,} vocab"
            )

            # Create the BM25 model and index the corpus
            retriever = bm25s.BM25()
            retriever.index(encoded_corpus)

            logger.info("Encoding Queries...")
            query_ids = list(queries.keys())
            self.results = {qid: {} for qid in query_ids}
            if excluded_ids:
                inverted_index = {corpus_id: index for index, corpus_id in enumerate(corpus_ids)}
            
            for qid, query_text in queries.items():
                query_token_str = self.encode(query_text, return_ids=False)
                weight_mask = np.ones(len(corpus_ids), dtype=np.float32)
                if excluded_ids:
                    excluded_ids_list = excluded_ids[qid]
                    mapped_excluded_id = [inverted_index[excluded_id] for excluded_id in excluded_ids_list]
                    weight_mask[mapped_excluded_id] = 0
                queries_result, queries_score = retriever.retrieve(
                    query_token_str, corpus=corpus_with_ids, k=top_k, weight_mask=weight_mask
                )
                doc_id_to_score = {}
                query_result = queries_result[0]
                scores = queries_score[0]
                
                # Iterate over results
                for ri in range(len(query_result)):
                    doc = query_result[ri]
                    score = scores[ri]
                    doc_id = doc["doc_id"]

                    doc_id_to_score[doc_id] = float(score)

                self.results[qid] = doc_id_to_score
            
            return self.results

        def encode(self, texts: list[str], **kwargs):
            """Encode input text as term vectors"""
            return bm25s.tokenize(texts, stopwords=self.stopwords, stemmer=self.stemmer)

    return BM25Search(**kwargs)


bm25_s = ModelMeta(
    loader=partial(bm25_loader, model_name="bm25s"),  # type: ignore
    name="bm25s",
    languages=["eng_Latn"],
    open_weights=True,
    revision="0_1_10",
    release_date="2024-07-10",  ## release of version 0.1.10
    n_parameters=None,
    memory_usage=None,
    embed_dim=None,
    license=None,
    max_tokens=None,
    reference=None,
    similarity_fn_name=None,
    framework=[],
    use_instructions=False,
)
