import requests
import json
from datetime import datetime

api_url = "http://localhost:11434/api/generate"
headers = {"content-Type": "application/json"}

print("AI Assistant is ready. Type your question below.")
print("Type 'exit' when finished. \n")

conversation_log = ""

while True:
    user_input = input("You:  ")

    if user_input.strip().lower() == "exit":
        print("Goodbye!")
        break

    full_prompt = conversation_log + f"\nUser: {user_input}\nAI:"

    data = {
        "model": "llama3.2",
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(
            api_url,
            headers=headers,
            data=json.dumps(data),
            timeout = 120
        )
        
        if response.status_code == 200:
            try:
                result = response.json()
                ai_reply = result.get("response", "(No response)")
                print(f"AI: {ai_reply.strip()}")

                conversation_log += f"\nUser: {user_input}\nAI: {ai_reply.strip()}"

                # Prevent conversation log from growing indefinitely
                if len(conversation_log) > 3000:
                    conversation_log = conversation_log[-3000:]

                try:
                    with open("chat_log.txt", "a", encoding="utf-8") as log_file:
                        ts = datetime.now().isoformat(timespec="seconds")
                        log_file.write(f"[{ts}] User:  {user_input}\n")
                        log_file.write(f"[{ts}] AI:  {ai_reply.strip()}\n\n")
                except OSError as e:
                    print(f"(Could not write chat_log.txt: {e})")
        
            except json.JSONDecodeError:
                print("Failed to parse response:", response.text)
        else:
            print(f"Error:      {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print("An error occurred", e)

