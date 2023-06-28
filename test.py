
import openai

import re
OPENAI_KEY = "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"
openai.api_key = OPENAI_KEY
if __name__ == "__main__":
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )

    print(completion.choices[0].message)