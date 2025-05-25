import mteb


model_name = "Salesforce/SFR-Embedding-2_R"
model = mteb.get_model(model_name)

benchmark = mteb.get_benchmark("MIRB")
evaluation = mteb.MTEB(tasks=benchmark)
results = evaluation.run(model, output_folder=f"results/mirb/{model_name}", encode_kwargs={"batch_size": 16, "max_length": 4096}, save_predictions=True)

task_score = {}

natural_proofs_tasks = ["ProofWikiPremiseRetrieval", "StacksPremiseRetrieval", "RealAnalysisPremiseRetrieval", "NumberTheoryPremiseRetrieval"]
natural_proofs_score = 0

for result in results:
    result_dict = result.to_dict()
    task_name = result_dict['task_name']
    score = result_dict['scores']['test'][0]['ndcg_at_10']
    if task_name in natural_proofs_tasks:
        natural_proofs_score += 100 * score
    else:
        task_score[task_name] = 100 * score

natural_proofs_score  = natural_proofs_score / len(natural_proofs_tasks)
task_score["NaturalProofsPremiseRetrieval"] = natural_proofs_score    

for task, score in task_score.items():
    print(f"{task}: {score}")

mirb_score = sum(task_score.values()) / len(task_score)
print(f"\nMIRB score: {mirb_score}")