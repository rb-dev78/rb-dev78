import requests
import json

# Send a prompt to the Ollama API

r= requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Convert 10 miles to kilometers"
    }
)

response = ""

# Ollama streams JSON responses line by line

for line in r.text.split('\n'):
    if line.strip() and '{' in line:
        response += json.loads(line).get("response", "")

print(response)
