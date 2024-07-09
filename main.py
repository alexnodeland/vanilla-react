import os
from openai import OpenAI
from agent import Agent
from actions import ActionRegistry
from tools import calculate, wikipedia
from query_engine import QueryEngine
import config

def main(question):
    """
    Initialize and configure the agent and action registry, and run the query engine with the provided question.
    """
    # Retrieve the OpenAI API key from environment variables or exit if not set
    api_key = os.getenv("OPENAI_API_KEY") or config.OPENAI_API_KEY
    if not api_key:
        exit("OPENAI_API_KEY not set")
    client = OpenAI(api_key=api_key)

    # Initialize the agent with the prompt from config
    agent = Agent(client, config.AGENT_SYSTEM_PROMPT)
    # Initialize the action registry and register available actions
    action_registry = ActionRegistry()
    action_registry.register("calculate", calculate)
    action_registry.register("wikipedia", wikipedia)

    # Initialize the query engine with the agent and action registry
    query_engine = QueryEngine(agent, action_registry, config.MAX_TURNS)

    # Run the query engine with the provided question
    query_engine.query(question)


if __name__ == "__main__":
    """
    Run a vanilla ReAct agent with a question provided as a command-line argument.
    """
    import sys

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = config.DEFAULT_QUESTION
    main(question)
