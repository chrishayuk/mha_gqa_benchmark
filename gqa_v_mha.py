import os
import dotenv
from openai import OpenAI

# Load environment variables from the .env file
dotenv.load_dotenv()

# Initialize the NVIDIA cloud client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
)

# get the model name
nemotron_model_name = "nvidia/nemotron-4-340b-reward"

def load_messages_from_file(file_path):
    """Load the entire content of the prompt file as a single user message."""
    with open("prompt.txt", 'r') as file:
        prompt = file.read().strip()

    """Load the entire content of the file as a single user message."""
    with open(file_path, 'r') as file:
        content = file.read().strip()

    # Set the messages
    messages = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": content}
    ]
    return messages

def get_completion_for_model(messages):
    """Get completion from the model for the given messages."""
    completion = client.chat.completions.create(
        model=nemotron_model_name,
        messages=messages
    )
    return completion

def store_completion_result(output_folder, model_name, completion):
    """Store the completion result in an output directory file."""
    output_file_path = os.path.join(output_folder, f"reward/{model_name}_reward.txt")
    with open(output_file_path, 'w') as file:
        if completion.choices and len(completion.choices) > 0:
            choice = completion.choices[0]
            if hasattr(choice, 'message') and isinstance(choice.message, list):
                for msg in choice.message:
                    if hasattr(msg, 'content'):
                        file.write("Message content:\n")
                        file.write(msg.content + "\n")
            if hasattr(choice, 'logprobs') and choice.logprobs:
                file.write("\nDetailed logprobs:\n")
                for logprob in choice.logprobs.content:
                    file.write(f"{logprob.token}: {logprob.logprob}\n")
        else:
            file.write("No choices found in the completion\n")

        if completion.usage:
            file.write("\nUsage:\n")
            file.write(f"Completion tokens: {completion.usage.completion_tokens}\n")
            file.write(f"Prompt tokens: {completion.usage.prompt_tokens}\n")
            file.write(f"Total tokens: {completion.usage.total_tokens}\n")

def process_files_in_folder(input_folder, output_folder):
    """Process all files in the input folder and store results in the output folder."""
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # Process only text files
            process_file(filename)

def process_file(model_name):
    filename = model_name + ".txt" 
    file_path = os.path.join(input_folder, filename)
    messages = load_messages_from_file(file_path)
    completion = get_completion_for_model(messages)
    store_completion_result(output_folder, model_name, completion)

# Define input and output folders
input_folder = './input'
output_folder = './output'

# Process all files in the input folder
#process_files_in_folder(input_folder, output_folder)
#process_file("gpt-3.5")
#process_file("gemini-1.5-advanced")
#process_file("gemma-2-27b")
#process_file("gemma-2-9b")
#process_file("gemma-1-7b")
#process_file("claude-3.5-sonnet")
#process_file("claude-3-opus")
#process_file("mistral-7b")
#process_file("mixtral-7b")
#process_file("mistral-small")
#process_file("mistral-next")
#process_file("mistral-large")
#process_file("llama-3-8b")
#process_file("llama-3-70b")
#process_file("llama-2-7b")
#process_file("llama-2-70b")
process_file("tinyllama")

