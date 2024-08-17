import google.generativeai as palm
import os

#@title Insert PaLM API Key here
palm.configure(api_key='XXXX')

# Use the palm.list_models function to find available models
# PaLM 2 available in 4 sizes: Gecko, Otter, Bison and Unicorn (largest)
# https://developers.generativeai.google/models/language
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
# print(model)

#simplest chatbot
# Set your input text
prompt = "Why is the sky blue?"
# prompt = "What is Quantum Computing? Explain like I'm 5."

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # temperature=0 >> more deterministic results // temperature=1 >> more randomness
    max_output_tokens=100
    # maximum length of response
)
print(completion.result)

#Code explainer
def get_completion(prompt):
  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=500,
      )
  response = completion.result
  return response

#simple promting
# input_code = f"""
# x = [1, 2, 3, 4, 5]
# y = [i**2 for i in x if i%2 == 0]
# print(y)
# """

input_code = f"""
def my_func(x):
    if x > 5:
        return "High"
    else:
        return "Low"
result = my_func(4) + my_func(6) + my_func(4)
print(result)
"""

prompt =f"""
Your task is to act as a Python Code Explainer.
I'll give you a Code Snippet.
Your job is to explain the Code Snippet step-by-step.
Also, compute the final output of the code.
Code Snippet is shared below, delimited with triple backticks:
```
{input_code}
```
"""

# print(prompt)
print(get_completion(prompt))
