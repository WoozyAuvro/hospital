from django.http import HttpResponse
from openai import OpenAI
import base64
import requests, json

def jsonContent(str):
  data = json.loads(str)
  try:
    resp = data["choices"][0]["message"]["content"]
    return resp
  except KeyError:
    return str
  
def process_chatbot_input(prompt):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "answer based on medical terms: {prompt}"},
        ],
        }
    ],
    max_tokens=300,
    )
    resp= response.choices[0].message.content
    print(resp)
#    responsep = f"Received image: {uploaded_image}, Prompt: {prompt}"
    return resp
