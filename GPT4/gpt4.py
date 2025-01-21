from openai import OpenAI

#Config OpenAI
client = OpenAI(api_key="g4a-aMWTFlPKVs2WcFmIY24Cc99XMakJQ9eJQB8", base_url="https://api.gpt4-all.xyz/v1")

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