from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MathlibRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="MathlibRetrieval",
        description="The task is to retrieve relevant natural language theorems given a mathematical query.",
        reference=None,
        dataset={
            "path": "hcju/mathlibretrieval",
            "revision": "c5109809d6b9e9704edde7e89faffeda3a066be1",
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
            "query": "Given a mathematical query, retrieve relevant theorems."
        },
    )
