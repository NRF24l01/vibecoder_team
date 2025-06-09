from . import Dialog
from helpers import extract_result, Logger, Timer


class Coder(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "deepseek-coder-v2:16b", logger: Logger = Logger()):
        super().__init__(
            host=host,
            model=model
        )
        self.logger = logger
    
    def code(self, prompt: str, task: str):
        self.prompt = prompt
        t = Timer()
        self.logger.info("Start processing task")
        model_response = self.ask(task)
        self.logger.info(f"Time elapsed {t.stop()}")
        comment, result = extract_result(model_response)
        # self.logger.info(f"Comment to answer: {comment}")
        return result
        
        

class Lead(Dialog):
    def __init__(self, host: str = 'http://localhost:11434', model: str = "gemma3:4b", logger: Logger = Logger()):
        super().__init__(
            host=host,
            model=model
        )
        self.logger = logger
    
    def think(self, prompt: str, task: str):
        self.prompt = prompt
        t = Timer()
        self.logger.info("Start processing task")
        model_response = self.ask(task)
        self.logger.info(f"Time elapsed {t.stop()}")
        comment, result = extract_result(model_response)
        return result

if __name__ == "__main__":
    with open("prompts/main_xml_output.txt", 'r') as f:
        prompt = f.read()
    task = "write an algorithm for finding a path through a wide detour"
    c = Coder()
    print(c.code(prompt, task, "code"))
    print("="*15)
    l = Lead()
    print(l.think(prompt, task, "lead"))
    print("="*15)
        
