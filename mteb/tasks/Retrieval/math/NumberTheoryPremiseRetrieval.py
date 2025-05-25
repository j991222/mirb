from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class NumberTheoryPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="NumberTheoryPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/numbertheoryps",
            "revision": "4607d837e0bfd917a4ace426a3156d16109063c8",
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
