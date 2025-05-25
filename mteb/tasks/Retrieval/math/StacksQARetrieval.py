from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class StacksQARetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="StacksQARetrieval",
        description="The task is to retrieve proofs of the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/stacksqa",
            "revision": "77b3ec1d53eb3ef97e825640a5cf09b6ea4b173d",
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
            "query": "Given a math theorem, retrieve its proof."
        },
    )
