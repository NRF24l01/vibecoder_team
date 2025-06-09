from ollama import Client
import time
import threading
import sys

class Dialog:
    def __init__(self, model: str, host: str = 'http://localhost:11434', prompt: str = "Output format - xml"):
        self.model = model
        self.prompt = prompt
        
        self.client = Client(
            host=host
        )
    
    def ask(self, q: str):
        def stopwatch(stop_event):
            start = time.time()
            while not stop_event.is_set():
                elapsed = time.time() - start
                spinner = "-/|\\"
                idx = int(elapsed * 10) % len(spinner)
                print(f"\r{spinner[idx]} {elapsed:.2f} {spinner[idx]}", end='', flush=True)
                time.sleep(0.1)
            # Print final time
            elapsed = time.time() - start
            print(f"\rElapsed: {elapsed:.2f}s", flush=True)

        stop_event = threading.Event()
        t = threading.Thread(target=stopwatch, args=(stop_event,))
        t.start()
        try:
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
        finally:
            stop_event.set()
            t.join()
        print(f"{response.message.content}")
        return response.message.content

if __name__ == "__main__":
    prompt = """
Please provide your answer ONLY in valid XML format with the following structure:
<response>
    <comment>Your thoughts or explanations about the solution</comment>
    <result>Your actual solution or response to the task</result>
</response>

Your response must:
- Contain only valid XML with no text before or after the XML tags
- Be properly formatted to be parsed by any standard XML reader
- Wrap your actual answer in the <response> tags
- Place any explanations in the <comment> tags

Do not include any non-XML content in your response.
"""
    task = "write an algorithm for finding a path through a wide detour"
    d = Dialog("starcoder2:7b", prompt=prompt) # starcoder2:7b  deepseek-coder-v2:16b
    d.ask(task)
    print("="*15)
    d = Dialog("deepseek-coder-v2:16b", prompt=prompt) # starcoder2:7b  deepseek-coder-v2:16b
    d.ask(task)