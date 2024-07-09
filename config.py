# OpenAI settings
# OPENAI_API_KEY = "<your-api-key>"
OPENAI_MODEL = "gpt-4"
OPENAI_TEMPERATURE = 0

# Agent settings
react_instructions = """
        You run in a loop of Thought, Action, PAUSE, Observation.
        At the end of the loop you output an Answer
        Use Thought to describe your thoughts about the question you have been asked.
        Use Action to run one of the actions available to you - then return PAUSE.
        Observation will be the result of running those actions.
    """
action_instructions = """
        Your available actions are:

        calculate:
        e.g. calculate: 4 * 7 / 3
        Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

        wikipedia:
        e.g. wikipedia: Django
        Returns a summary from searching Wikipedia

        Always look things up on Wikipedia if you have the opportunity to do so.
    """
react_example = """
        Example session:

        Question: What is the capital of France?
        Thought: I should look up France on Wikipedia
        Action: wikipedia: France
        PAUSE

        You will be called again with this:

        Observation: France is a country. The capital is Paris.

        You then output:

        Answer: The capital of France is Paris
    """
AGENT_SYSTEM_PROMPT = f"{react_instructions}\n\n{action_instructions}\n\n{react_example}".strip()

MAX_TURNS = 5

# QueryEngine settings
ACTION_REGEX = r"^Action: (\w+): (.*)$"

# Default question
DEFAULT_QUESTION = "What is category theory?"