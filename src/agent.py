from ollama import chat
from src.analyst import Analyst
from src.utils import Utils
from src.loggers import Logger



utils = Utils
analysis = Analyst()

logger = Logger()
logger.add_ecs_formatter()
logger.add_elasticsearch_handler()


class Agent:
    def __init__(self, data): #data=pd.DataFrame()
        self.model = 'ollama'
        self.data = data
        self.role = 'user'
        self.response=None


    def call_ollama(self, question):
        logger.emit_log("call_ollama.start", question=question, rows=len(self.data))

        if len(self.data) == 0:
            self.response = f"Data could not be fetched, please try again"
            analysis.save_fallback_metadata(self.response, question)
            logger.emit_log("call_ollama.empty_data", question=question)
            return self.response

        extract_date = utils.extract_date(question)

        if extract_date:
            self.response = self.call_simple_response(question)
            analysis.save_agent_response(self.response, question)
            logger.emit_log("call_ollama.success", question=question)
            return self.response.message.content
        elif utils.is_weekend(str(extract_date)):
            self.response = f"Please enter a date that doesn't fall on a weekend"
            analysis.save_fallback_metadata(self.response, question)
            logger.emit_log("call_ollama.weekend_rejected", question=question)
            return self.response

        return self.response


    def call_simple_response(self, question):
        logger.emit_log("call_simple_response.start", question=question, model='llama3')
        self.response = chat(
            model='llama3',
            stream=False,
            messages=[
                {
                    'role': self.role,
                    'content': f"Here is the data : \n{self.data}/n {question}",
                },
            ],
        )
        logger.emit_log("call_simple_response.complete", question=question)
        return self.response







