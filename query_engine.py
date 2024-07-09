import re
import config

class QueryEngine:
    """
    Manage a conversation loop with an agent, execute actions based on the agent's responses, and update the conversation context with observations from those actions.
    """

    def __init__(self, agent, action_registry, max_turns=5):
        # Initialize the query engine with an agent, action registry, and maximum turns
        self.agent = agent
        self.action_registry = action_registry
        self.max_turns = max_turns
        # Compile a regular expression to match actions in the agent's response
        self.action_re = re.compile(config.ACTION_REGEX)

    def query(self, question):
        """
        Run the conversation loop with the agent to dynamically process and respond to questions.
        """
        # Initialize the turn counter and the next prompt with the question
        i = 0
        next_prompt = question
        while i < self.max_turns:
            i += 1
            # Get the agent's response to the current prompt
            result = self.agent(next_prompt)
            print(result)
            # Find all actions in the agent's response
            actions = [
                self.action_re.match(a)
                for a in result.split("\n")
                if self.action_re.match(a)
            ]
            if actions:
                # If there are actions, execute the first one
                action_name, action_input = actions[0].groups()
                action = self.action_registry.get(action_name)
                if not action:
                    raise Exception(f"Unknown action: {action_name}: {action_input}")
                print(f" -- running {action_name} {action_input}")
                observation = action.execute(action_input)
                print("Observation:", observation)
                # Update the next prompt with the observation
                next_prompt = f"Observation: {observation}"
            else:
                # If no actions are found, exit the loop
                return