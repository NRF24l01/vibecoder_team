import yaml
from ollama import Client
from pathlib import Path

# === Config ===
CONFIG_PATH = "config.yaml"
HOST = "http://127.0.0.1:11434"

with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

AGENTS = config['teams']

client = Client(host=HOST)

# === CLI ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python llm_pipeline_runner.py \"Create an online course platform\"")
        exit(1)

    user_input = sys.argv[1]
