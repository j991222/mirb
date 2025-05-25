from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class StacksPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="StacksPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/stacksps",
            "revision": "dc05e6bda28f6fe7fa659f03bc4f86b7f7d60ea1",
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
