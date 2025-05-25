from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class ProofWikiQARetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="ProofWikiQARetrieval",
        description="The task is to retrieve proofs of the given theorem.",
        reference=None,
        dataset={
            "path": "hcju/proofwikiqa",
            "revision": "595dfde06810d59921566d3b2091aaccfb0793d5",
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
