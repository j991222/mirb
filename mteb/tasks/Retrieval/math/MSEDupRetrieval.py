from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MSEDupRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="MSEDupRetrieval",
        description="The task is to retrieval duplicate questions for the given MSE question.",
        reference=None,
        dataset={
            "path": "hcju/msedup",
            "revision": "fda2c63e29fbd6e09426d8ad87bfe41f9e5dedf3",
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
            "query": "Given a math question, retrieve questions that are duplicates of the given one"
        },
    )
