from ollama import Client

class Dialog:
    def __init__(self, model: str, host: str = 'http://localhost:11434', prompt: str = "Выдавай чётко струтурированый ответ в формате xml"):
        self.model = model
        self.prompt = prompt
        
        self.client = Client(
            host=host
        )
    
    def ask(self, q: str):
        response = self.client.chat(model=self.model, messages=[
            {
                'role': 'system',
                'content': self.prompt,
            },
            {
                'role': 'user',
                'content': q,
            },
        ])
        print(response.message.content)

if __name__ == "__main__":
    d = Dialog("gemma3:4b")
    d.ask("Ты кто?")