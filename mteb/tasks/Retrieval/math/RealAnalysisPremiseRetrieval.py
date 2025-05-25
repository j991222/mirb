from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class RealAnalysisPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="RealAnalysisPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/realanalysisps",
            "revision": "87a45bc950b2be637b294263db799043a5d0d5e4",
            "dynamic_corpus": True
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
