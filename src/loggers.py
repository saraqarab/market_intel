import logging
import ecs_logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(logging.DEBUG)

    def add_ecs_formatter(self):
        handler = logging.StreamHandler()
        handler.setFormatter(ecs_logging.StdlibFormatter())
        self.logger.addHandler(handler)


    def emit_log(self, msg :str):
        self.logger.debug(msg="Example message!")


