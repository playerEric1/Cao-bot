import openai
import dotenv
import os

dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def get_gpt3(prompt):
    # create a completion
    print(prompt)
    completion = openai.Completion.create(
        model="text-ada-001",
        prompt=prompt,
        temperature=1,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print the completion
    print(completion)
    return completion["choices"][0]["text"]
