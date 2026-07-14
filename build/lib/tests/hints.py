from eos_workflow.convergency import convergency_workflows
from jobflow import run_locally

element = "H"
ecuts = [10, 20, 30, 40]
configuration = 'FCC'
pseudo = "ONCVPSP-PBE-SR-PDv0.4:standard"
jobs = convergency_workflows(
    element,
    configuration,
    ecuts=ecuts,
    pseudos=pseudo,
)

res = run_locally(jobs, create_folders=True)
# res = submit_flow(jobs)
print(res)
print(element)
print(pseudo)
