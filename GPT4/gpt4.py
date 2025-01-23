from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Carica le variabili di ambiente dal file .env
load_dotenv()

#Config OpenAI
client = AzureOpenAI(api_key=os.getenv('api_key'), azure_endpoint=os.getenv('azure_endpoint'),api_version=os.getenv('api_version'))

#Return Simple Response By User
def response_by_user(message):
    #def response
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
        stream=False,
    )
    #return response
    return response.choices[0].message.content
print(response_by_user("ciao"))