import logging
# from langchain_ollama import ChatOllama

import subprocess

from ollama import ChatResponse
from ollama import chat


class Agent:
    def __init__(self, model='ollama'):
        self.model = model

    def check_ollama_installation(self):
        if print(self.model) :
            pass
        else:
            logging.log(msg="Ollama module not installed", level=2)
            logging.log(msg="Initiating model installation", level=2)


    def call_ollama(self, role= 'user', content = 'Why is the sky blue?'):
        role = role.lower()

        response: ChatResponse = chat(model='gemma3',  stream = True, messages=[
            {
                'role': role,
                'content': content,
            },
        ])
        print(response['message']['content'])

    def install_model(self):
        capture_output = True
        subprocess.call(['curl -fsSL https://ollama.com/install.sh | sh'])
        logging.log(msg="Initiating model installation", level=2)
        subprocess.call(args='ollama pull gemma3')
        subprocess.call(args='ollama run gemma3')




