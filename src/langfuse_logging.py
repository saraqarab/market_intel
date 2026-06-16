from dotenv import load_dotenv
load_dotenv()

from langfuse import get_client


class LangfuseLogging():
    def __init__(self):
        self.langfuse = get_client()
        self._verify_connection()
        self.create_span()

    def _verify_connection(self):
        if self.langfuse.auth_check():
            print("Langfuse client is authenticated and ready!")
        else:
            print("Authentication failed. Please check your credentials and host.")

    def create_span(self):
        with self.langfuse.start_as_current_observation(as_type="span", name="process-request") as span:
            # Your processing logic here
            span.update(output="Processing complete")
            # Create a nested generation for an LLM call
            with self.langfuse.start_as_current_observation(as_type="generation", name="llm-response",
                                                       model="gpt-3.5-turbo") as generation:
                # Your LLM call logic here
                generation.update(output="Generated response")

        self.langfuse.flush()










