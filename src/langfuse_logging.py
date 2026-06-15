from langfuse import get_client
from dotenv import load_dotenv
load_dotenv()


class LangfuseLogging:
    def __init__(self):
        self.langfuse = get_client()
        self._verify_connection()
        self.initiate_spans()
        self._flush_langfuse()

    def initiate_spans(self):
        """If trace covers an entire request, span covers an individual step"""
        with self.langfuse.start_as_current_observation(as_type="span", name="process-request") as span:
            span.update(output="Processing complete")

            with self.langfuse.start_as_current_observation(as_type="generation",name="local llama3",model="llama3") as generation:
                generation.update(output="Generated response")

    def _flush_langfuse(self):
        self.langfuse.flush()

    def _verify_connection(self):
        if self.langfuse.auth_check():
            print("Langfuse client is authenticated and ready!")
        else:
            print("Authentication failed. Please check your credentials and host.")

