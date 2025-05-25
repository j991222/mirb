from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HolPremiseRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="HolPremiseRetrieval",
        description="The task is to retrieve useful references (theorems, lemmas, definitions) for proving the given HOL conjecture.",
        reference=None,
        dataset={
            "path": "hcju/holps",
            "revision": "a2272075a0e0789e3ee1ac0694104d234fd701c4",
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
            "query": "Given a HOL conjecture, retrieve the declarations that are useful for proving it."
        },
    )
