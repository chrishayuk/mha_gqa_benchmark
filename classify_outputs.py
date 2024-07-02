import os
import dotenv
import openai

# Load environment variables from .env file
dotenv.load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# File and directory paths
original_prompt_file = "prompt.txt"
directory = "./input"

# Read the original prompt
with open(original_prompt_file, 'r') as file:
    original_prompt = file.read()

# Initialize an empty string to hold the concatenated details
all_file_details = ""

# Iterate over each file in the directory and read their contents
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        with open(os.path.join(directory, filename), 'r') as file:
            content = file.read()
            file_details = f"Filename: {filename}\n{content}\n\n"
            all_file_details += file_details

# Prepare the prompt to send to GPT-4 model
# Prepare the prompt to send to GPT-4 model
prompt = (
    f"The following is an original prompt and several responses to it. Based on the quality of the responses looking at whether the response is broad, narrow, integrated, segmented, fluid, unfluid, list-like.  Using this information determine from the response whether the model is likely a Grouped Query Attention (GQA) model or Multi Headed Attention (MHA) model\n\n"
    f"Original Prompt:\n{original_prompt}\n\n"
    f"Responses:\n\n{all_file_details}"
)
print(prompt)

# # Send the prompt to GPT-4 model and get the response
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     max_tokens=150,
#     n=1,
#     stop=None,
#     temperature=0.7
# )

# # Print the response from the model
# print(response.choices[0].text.strip())
