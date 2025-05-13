import requests
import time
import random
import re

API_KEY = ''  # ← Встав API-ключ сюди
API_URL = 'https://inference-api.nousresearch.com/v1/chat/completions'
MODEL_NAME = 'Hermes-3-Llama-3.1-70B'

# Зчитування та обробка питань
with open('questions.txt', 'r', encoding='utf-8') as f:
    raw_questions = f.readlines()

# Очистка питань від нумерації
def clean_question(q):
    return re.sub(r'^\s*\d+[\.\)\-]?\s*', '', q).strip()

questions = [clean_question(q) for q in raw_questions if q.strip()]
random.shuffle(questions)

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

for question in questions:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    print(f"\n🟢 Запит: {question}")
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        content = response.json()['choices'][0]['message']['content']
        print(f"🔵 Відповідь: {content}")
    else:
        print(f"🔴 Помилка {response.status_code}: {response.text}")

    time.sleep(20)
