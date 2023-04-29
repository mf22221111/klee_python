# import openai
#
# # Set your API key
# openai.api_key = "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"
# # Use the GPT-3 model
# completion = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt="Once upon a time, in a land far, far away, there was a princess who...",
#     max_tokens=1024,
#     temperature=0.5
# )
# # Print the generated text
# print(completion.choices[0].text)
import os
#
import openai
# os.environ["http_proxy"] = "http://127.0.0.1:33210"
# os.environ["https_proxy"] = "http://127.0.0.1:33210"
# Apply the API key
openai.api_key = "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"

# Define the text prompt
prompt = "In a shocking turn of events, scientists have discovered that "

# Generate completions using the API
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the message from the API response
message = completions.choices[0].text
print(message)
# import os
# import openai
# os.environ["http_proxy"] = "http://127.0.0.1:33210"
# os.environ["https_proxy"] = "http://127.0.0.1:33210"
# openai.api_key = "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"
#
# model_engine = "text-davinci-002"
# prompt = "Hi, how are you doing today?"
#
# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.7,
# )
#
# message = completions.choices[0].text
# print(message)

import os
# import openai
# openai.organization = "org-FtwOFrKmXqzR3Ybnau4QsXsf"
# openai.api_key = "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"
# openai.Model.list()