from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class IsabellePremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="IsabellePremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given Isabelle proof state.",
        reference=None,
        dataset={
            "path": "hcju/isabelleps",
            "revision": "9370d325d494b7c42a927242c857f8465c23deb6",
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
            "query": "Given an Isabelle proof state, retrieve the declarations that are useful for proving it."
        },
    )
