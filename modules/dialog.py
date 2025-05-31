from ollama import Client

class Dialog:
    def __init__(self, model: str, host: str = 'http://localhost:11434', prompt: str = "Output format - xml"):
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
    task = "write an algorithm for finding a path through a wide detour"
    d = Dialog("starcoder2:7b") # starcoder2:7b  deepseek-coder-v2:16b
    d.ask(task)
    print("="*15)
    d = Dialog("deepseek-coder-v2:16b") # starcoder2:7b  deepseek-coder-v2:16b
    d.ask(task)