from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MSEQARetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="MSEQARetrieval",
        description="The task is to retrieve solutions of the given problem.",
        reference=None,
        dataset={
            "path": "hcju/mseqa",
            "revision": "056c9ccf55e4850967e53e0c5267ca40c6c321c0",
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
            "query": "Given a math problem, retrieve its solution."
        },
    )
