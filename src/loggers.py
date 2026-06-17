import logging
import os

import ecs_logging
from elasticsearch import Elasticsearch


class ElasticsearchHandler(logging.Handler):
    """Ships ECS-formatted log records to Elasticsearch so Kibana can display them."""

    def __init__(self, host: str, index: str):
        super().__init__()
        self.index = index
        self.client = Elasticsearch(hosts=[host])

    def emit(self, record):
        try:
            document = self.format(record)
            self.client.index(index=self.index, document=document)
        except Exception:
            self.handleError(record)


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(logging.DEBUG)

    def add_ecs_formatter(self):
        handler = logging.StreamHandler()
        handler.setFormatter(ecs_logging.StdlibFormatter())
        self.logger.addHandler(handler)

    def add_elasticsearch_handler(self, host: str = None, index: str = "market-intel-logs"):
        host = host or os.environ.get("ELASTICSEARCH_HOST", "http://localhost:9200")
        handler = ElasticsearchHandler(host=host, index=index)
        handler.setFormatter(ecs_logging.StdlibFormatter())
        self.logger.addHandler(handler)

    def emit_log(self, msg: str, **fields):
        self.logger.debug(msg=msg, extra=fields)
