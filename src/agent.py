from src.yfinance_adapter import YFinanceAdapter
from ollama import ChatResponse
from ollama import chat
import subprocess
import logging
import json
import time


class Agent:
    def __init__(self, data):
        self.model = 'ollama'
        self.data = data


    def check_ollama_installation(self):
        if print(self.model) :
            pass
        else:
            logging.log(msg="Ollama module not installed", level=2)
            logging.log(msg="Initiating model installation", level=2)


    def call_ollama(self, question):
        role = 'user'
        response: ChatResponse = chat(model='gemma3',  stream = False, messages=[
            {
                'role': role,
                'content': f"Here is the data : \n{self.data}/n {question}",
            },
        ])
        self.save_agent_response(response)
        print(response.message.content)


    def install_model(self):
        """DIY Later"""
        capture_output = True
        subprocess.call(['curl -fsSL https://ollama.com/install.sh | sh'])
        logging.log(msg="Initiating model installation", level=2)
        subprocess.call(args='ollama pull gemma3')
        subprocess.call(args='ollama run gemma3')

    def save_agent_response(self, response):
        meta_data = dict()
        meta_data['timestamp'] = time.time()
        meta_data['model'] = str(response.model)
        meta_data['created_at'] = str(response.created_at)
        meta_data['done'] = str(response.done)
        meta_data['done_reason'] = str(response.done_reason)
        meta_data['content'] = str(response.message.content)
        meta_data['total_duration'] = str(response.total_duration)
        meta_data['load_duration'] = str(response.load_duration)
        meta_data['prompt_eval_count'] = str(response.prompt_eval_count)
        meta_data['prompt_eval_duration'] = str(response.prompt_eval_duration)
        meta_data['eval_count'] = str(response.eval_count)
        meta_data['eval_duration'] = str(response.eval_duration)
        with open(f"{time.time()}.json", "w") as json_file:
            json.dump(meta_data, json_file, indent=4)





