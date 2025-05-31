from . import Dialog
from helpers import extract_result, Logger


class Coder(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "deepseek-coder-v2:16b", logger: Logger = Logger()):
        super().__init__(
            host=host,
            model=model
        )
        self.logger = logger
    
    def code(self, prompt: str, task: str, output_tag: str):
        self.prompt = prompt
        model_response = self.ask(task)
        comment, result = extract_result(model_response)
        

class Lead(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "gemma3:4b"):
        super().__init__(
            host=host,
            model=model
        )
        
