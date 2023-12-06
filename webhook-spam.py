import requests
import json
import time

with open('webhook.txt', 'r') as file:
    webhook_urls = file.read().splitlines()

message = input("Enter your custom message: ")

try:
    num_messages = int(input("Enter the number of times to send the message to each webhook: "))
except ValueError:
    print("Please enter a valid number of messages.")
    exit()

message_delay = 1

for _ in range(num_messages):
    for webhook_url in webhook_urls:
        payload = {
            'content': message
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 204:
            print(f"Message sent successfully to {webhook_url}: {message}")
        else:
            print(f"Failed to send message to {webhook_url}: {message}")

        time.sleep(message_delay)
