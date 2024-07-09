from openai import OpenAI
import config

class Agent:
    """
    Creates a chat completion using the OpenAI client to generate a response based on the conversation history.
    """

    def __init__(self, client, system=""):
        # Initialize the agent with an OpenAI client and an optional system message
        self.client = client
        self.system = system
        self.messages = []
        if self.system:
            # Add the system message to the list of messages if provided
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        """
        Handle user input, generate a response, and maintain the conversation history.
        """
        # Add the user's message to the list of messages
        self.messages.append({"role": "user", "content": message})
        # Execute the agent's response
        result = self.execute()
        # Add the agent's response to the list of messages
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        """
        Generate a response from the LLM.
        """
        # Create a chat completion using the OpenAI client
        completion = self.client.chat.completions.create(
            model=config.OPENAI_MODEL, temperature=config.OPENAI_TEMPERATURE, messages=self.messages
        )
        # Return the content of the first choice's message
        return completion.choices[0].message.content
