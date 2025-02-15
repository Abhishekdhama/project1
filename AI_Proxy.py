import requests

AIPROXY_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDA3NjJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.qoip96xLfJ0icQvJcFoxJlNNrDD_UZeMqZTISFlWOwk'

def add_two_numbers_with_ai_proxy(num1, num2):
    proxy_url = 'https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {AIPROXY_TOKEN}'  
    }

    payload = {
        'model': 'gpt-4o-mini',
        "messages": [
            {'role': 'system', 'content': 'You are a Python calculator. Add two numbers when asked.'},
            {'role': 'user', 'content': f'Add {num1} and {num2}'}
        ],
        'temperature': 0,
        'max_tokens': 50
    }

    response = requests.post(url=proxy_url, headers=headers, json=payload)

    if response.ok:
        ai_response = response.json()
        result = ai_response['choices'][0]['message']['content'].strip()
        return result

    return f'Error Fetching the sum, Status_code = {response.status_code}'

num1 = 5
num2 = 3
print(f"Addition of {num1} and {num2} is: {add_two_numbers_with_ai_proxy(num1, num2)}")
