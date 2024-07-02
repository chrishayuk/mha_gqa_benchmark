import dotenv
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent

# load environment variables .env file
dotenv.load_dotenv()

# llm
llm = OpenAI(model="gpt-4o")

# define sample Tool
def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

# File and directory paths
original_prompt_file = "test.txt"

# Read the original prompt
with open(original_prompt_file, 'r') as file:
    original_prompt = file.read()

# initialize llm
llm = OpenAI(model="gpt-4o")

# initialize ReAct agent
agent = ReActAgent.from_tools([], llm=llm, verbose=True)

# chat
agent.chat(original_prompt  )