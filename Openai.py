import openai

# set up API key
openai.api_key = "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"

# generate text with the GPT-3 model
prompt = "python chatgpt code example"
model_engine = "text-davinci-002"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
