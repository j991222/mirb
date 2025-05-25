from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class WikiFormulaRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="WikiFormulaRetrieval",
        description="The task is to retrieve relevant formulas given a query formula.",
        reference=None,
        dataset={
            "path": "hcju/wikiformula",
            "revision": "81ffeb15150f5c4619c088df9a458859af873613",
            "dynamic_corpus": True,
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
            "query": "Given a math formula, retrieve relevant formulas."
        },
    )
