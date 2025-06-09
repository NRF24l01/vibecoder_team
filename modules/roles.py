from . import Coder, Lead
from helpers import Logger, XMLTemplateRenderer
from lxml import etree as ET

class Communicator(Lead):
    def __init__(self, host: str = 'http://localhost:11434', logger: Logger = Logger()):
        super().__init__(host=host, logger=logger)
        self.logger = logger
        with open("prompts/main_xml_output.txt", 'r') as f:
            self.main_prompt = f.read()
    
    def process_result(self, result: str):
        print("Processing result:", result)
        # Load result string to xml
        parser = ET.XMLParser(recover=True)
        tree = ET.fromstring(result.encode('utf-8'), parser=parser)
        
        task = tree.find("new_task").text.strip()
        featues = tree.find("features")
        if task is None:
            raise ValueError("Invalid XML format: Missing <new_task> or <features> elements")\
        
        features_converted = []
        if featues is not None:
            for feature in featues:
                if feature.tag == "feature":
                    features_converted.append({
                        "name": feature.attrib.get("name"),
                        "value": feature.text
                    })
        return task, features_converted
            
    
    def work(self, task: str):
        template = XMLTemplateRenderer("prompts/communicator.xml")
        prompt = self.main_prompt + template.render(context={"task": task})
        self.logger.info("Asked communicator")
        response = self.think(prompt, f"<task>{task}</task>")
        self.logger.info("Communicator response received")
        task, features = self.process_result(response)
        return task, features


if __name__ == "__main__":
    communicator = Communicator()
    task = "write an algorithm for finding a path through a wide detour"
    task, features = communicator.work(task)
    print(task, features)

        