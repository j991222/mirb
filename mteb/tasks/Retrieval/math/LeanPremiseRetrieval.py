from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class LeanPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="LeanPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given Lean 4 proof state.",
        reference=None,
        dataset={
            "path": "hcju/leanps",
            "revision": "7d07605ffd06738555b3a4ed5edea3beccc7363d",
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
            "query": "Given a Lean 4 proof state, retrieve the declarations that are useful for proving it."
        },
    )
