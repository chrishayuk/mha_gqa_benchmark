import os
import dotenv
from openai import OpenAI

# load environment variables .env file
dotenv.load_dotenv()

# Directory containing the files
directory = "./output/reward"

# Initialize an empty string to hold the concatenated details
all_file_details = ""

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        with open(os.path.join(directory, filename), 'r') as file:
            # Read the content of the file
            content = file.read()
            # Concatenate the file name and its content
            file_details = f"Filename: {filename}\n{content}\n\n"
            all_file_details += file_details

# Prepare the prompt to send to GPT-4 model
prompt = f"Please rank the following files based on their contents:\n\n{all_file_details}"

print(prompt)

# # Initialize NVIDIA cloud client
# client = OpenAI()

# # Get the model name
# model_name = "gpt-4o"

# # Set the messages
# messages = [{"role": "user", "content": prompt}]

# # Setup the completion
# completion = client.chat.completions.create(
#     model=model_name,
#     messages=messages
# )

# print(completion)

# # Extract and print the content
# if completion.choices and len(completion.choices) > 0:
#     choice = completion.choices[0]
#     if hasattr(choice, 'message') and isinstance(choice.message, list):
#         for msg in choice.message:
#             if hasattr(msg, 'content'):
#                 print("Message content:")
#                 print(msg.content)
#     if hasattr(choice, 'logprobs') and choice.logprobs:
#         print("\nDetailed logprobs:")
#         for logprob in choice.logprobs.content:
#             print(f"{logprob.token}: {logprob.logprob}")
# else:
#     print("No choices found in the completion")

# # Print usage information
# if completion.usage:
#     print("\nUsage:")
#     print(f"Completion tokens: {completion.usage.completion_tokens}")
#     print(f"Prompt tokens: {completion.usage.prompt_tokens}")
#     print(f"Total tokens: {completion.usage.total_tokens}")
