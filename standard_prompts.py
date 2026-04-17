import requests
import json

api_url = "http://localhost:11434/api/generate"
headers = {"content-Type": "application/json"}
data = {
    "model": "llama3.2",
    "prompt": "Is the Earth round or a different shape?",
    "stream": False
    }
try:
    response = requests.post(api_url, headers=headers, data=json.dumps(data), timeout= 60)
    if response.status_code ==200:
        try:
            result = response.json()
            print(f"Response: {result.get('response', 'No response key in JSON' )}")
        except:
            print("Failed to parse JSON response:", response.txt)

    else:
        print(f"Error:      {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print("An error occurred", e)

