from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MSEFormulaRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="MSEFormulaRetrieval",
        description="The task is to retrieve relevant formulas given a query formula and its context.",
        reference=None,
        dataset={
            "path": "hcju/mseformula",
            "revision": "6f9ff65757f6657f4f6083d1caecee261396c6f3",
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
            "query": "Given a math formula and its context, retrieve relevant formulas."
        },
    )
