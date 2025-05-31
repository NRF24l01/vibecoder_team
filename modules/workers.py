from . import Dialog
from helpers import extract_result, Logger, Timer


class Coder(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "deepseek-coder-v2:16b", logger: Logger = Logger()):
        super().__init__(
            host=host,
            model=model
        )
        self.logger = logger
    
    def code(self, prompt: str, task: str, output_tag: str):
        self.prompt = prompt
        t = Timer()
        self.logger.info("Start processing task")
        model_response = self.ask(task)
        self.logger.info(f"Time elapsed {t.stop()}")
        comment, result = extract_result(model_response)
        self.logger.info(f"Comment to answer: {comment}")
        return result
        
        

class Lead(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "gemma3:4b", logger: Logger = Logger()):
        super().__init__(
            host=host,
            model=model
        )
        self.logger = logger
    
    def think(self, prompt: str, task: str, output_tag: str):
        self.prompt = prompt
        t = Timer()
        self.logger.info("Start processing task")
        model_response = self.ask(task)
        self.logger.info(f"Time elapsed {t.stop()}")
        comment, result = extract_result(model_response)
        self.logger.info(f"Comment to answer: {comment}")
        return result
        
