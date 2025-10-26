
import os
import json
import time
from rich import print
from mistralai.client import TrainingParameters
from mistralai.models.chat_completion import ChatMessage
from mistralai.models.jobs import WandbIntegrationIn


api_key=os.environ("MISTRAL_API_KEY")
client=MistralClient(api_key=api_key)

def pprint(obj):
    print(json.dumps(obj.dict(),indent=4))

##1. Uplad the dataset
with open("ultrachat_chunk_train.json","rb") as f:
    ultrachat_chunk_train=client.files.create(file=("ultrachat_chunk_train.json",f))
with open("ultrachat_chunk_eval.json","rb") as f:
    ultrachat_chunk_train=client.files.create(file=("ultrachat_chunk_eval.json",f))
     
print("Data:")
pprint(ultrachat_chunk_train)

## 2. Creating a fine tuning job

create_jobs=client.jobs.create(model="open-mistal-7b",training_files=[ultrachat_chunk_train.id],validation_files=[ultra_chunk_eval.id],
                               hyperparameters=TrainingParameters(training_steps=10,learning_rate=0.001),integrations=[WandbIntegrationIn(project="test_ft_api",run_name="test",api_key=os.environ.get("WANDB_API_KEY")).dict()])

## 3. check the status of the job
jobs=client.jobs.list()
pprint(jobs)
retrieved_jobs=client.jobs.retrieve(create_jobs.id)
while retrieved_jobs in ["RUNNING","QUEUED"]:
    retrieved_jobs=client.jobs.retrieve(create_jobs.id)
    print(retrieved_jobs)
    print(f" Job is {retrieved_jobs.status} wait for 10 seconds")
    time.sleep(10)
pprint(retrieved_jobs)

## 5. use fientuned model
chat_response=client.chat(model=retrieved_jobs.fine_tuned_model,messages=[ChatMessage(role='User',content='What is the best French Novel')])
print('\nTesting Fine Tuned Model:')
print(chat_response)