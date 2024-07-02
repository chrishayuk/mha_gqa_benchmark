import dotenv
from openai import OpenAI

# load environment variables .env file
dotenv.load_dotenv()

# initialize nvidia cloud client
client = OpenAI(
   base_url="https://integrate.api.nvidia.com/v1",
)

# get the model name
model_name = "nvidia/nemotron-4-340b-reward"

# Set the messages
messages = [
    {"role": "user", "content": "Who is Ada Lovelace?"},
    {"role": "assistant", "content": "She was the mayor of Paris"}
]

# setup the completion
completion = client.chat.completions.create(
   model=model_name,
   messages=messages
)

# Extract and print the content
if completion.choices and len(completion.choices) > 0:
    choice = completion.choices[0]
    if hasattr(choice, 'message') and isinstance(choice.message, list):
        for msg in choice.message:
            if hasattr(msg, 'content'):
                print("Message content:")
                print(msg.content)
    if hasattr(choice, 'logprobs') and choice.logprobs:
        print("\nDetailed logprobs:")
        for logprob in choice.logprobs.content:
            print(f"{logprob.token}: {logprob.logprob}")
else:
    print("No choices found in the completion")

# Print usage information
if completion.usage:
    print("\nUsage:")
    print(f"Completion tokens: {completion.usage.completion_tokens}")
    print(f"Prompt tokens: {completion.usage.prompt_tokens}")
    print(f"Total tokens: {completion.usage.total_tokens}")