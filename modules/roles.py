from . import Coder, Lead
from helpers import Logger, XMLTemplateRenderer

class Communicator(Lead):
    def __init__(self, host: str = 'http://localhost:11434', logger: Logger = Logger()):
        super().__init__(host=host, logger=logger)
        self.logger = logger
        with open("prompts/main_xml_output.txt", 'r') as f:
            self.main_prompt = f.read()
    
    def work(self, task: str):
        template = XMLTemplateRenderer("prompts/communicator.xml")
        prompt = self.main_prompt + template.render(context={"task": task})
        self.logger.info("Asked communicator")
        response = self.think(prompt, f"<task>{task}</task>")
        self.logger.info("Communicator response received")
        return response


if __name__ == "__main__":
    communicator = Communicator()
    task = "write an algorithm for finding a path through a wide detour"
    response = communicator.work(task)
    print(response)

        