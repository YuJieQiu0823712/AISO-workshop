"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent
from my_agent.tools.calculator import calculator_tool

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash",
    name="agent",
    description="A helpful assistant.",
    instruction=(
        "You are a helpful assistant that answers "
        "questions directly and concisely. "
        "Explain your reasoning step by step."
        "Use the calculator tool when the user asks for numerical arithmetic calculations."
    ),
    tools=[calculator_tool],
    sub_agents=[],
)

if __name__ == "__main__":
    result=calculator_tool("add", 1, 2)
    print(result)