from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MODupRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="MODupRetrieval",
        description="The task is to retrieval duplicate questions for the given MathOverflow question.",
        reference=None,
        dataset={
            "path": "hcju/modup",
            "revision": "b123b60d6ccaad16eb0305f3f35e14dd557c0962",
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
