from openai import OpenAI, AzureOpenAI, AsyncAzureOpenAI
from dotenv import load_dotenv
import os

# Carica le variabili di ambiente dal file .env
load_dotenv()

#Config OpenAI
client = OpenAI(api_key="g4a-96vBKjQ1Zhwesf9U5r7OSPgRv1miGsykNQm", base_url="https://api.gpt4-all.xyz/v1")

#Return Simple Response By User
def response_by_user(message):
    #def response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
        stream=False,
    )
    #return response
    return response.choices[0].message.content

print(response_by_user("ciao"))