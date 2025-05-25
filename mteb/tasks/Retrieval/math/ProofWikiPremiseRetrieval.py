from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class ProofWikiPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="ProofWikiPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/proofwikips",
            "revision": "a54bdf7d580390e1d35ae99c728f56cd842f72ec",
            "dynamic_corpus": False
        },
        type="Retrieval",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a math theorem, retrieve useful references, such as theorems, lemmas, and definitions, that are useful for proving the given theorem."
        },
    )
