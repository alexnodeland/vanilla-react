class Action:
    """
    Define an action that can be executed by an agent.
    """

    def __init__(self, name, func):
        # Initialize the action with a name and a function to execute
        self.name = name
        self.func = func

    def execute(self, input_data):
        # Execute the function with the provided input data
        return self.func(input_data)


class ActionRegistry:
    """
    Register new actions and retrieve existing ones.
    """

    def __init__(self):
        # Initialize an empty dictionary to store actions
        self.actions = {}

    def register(self, name, func):
        """
        Registers a new action with the given name and function, allowing the system to dynamically extend its capabilities.
        """
        # Register a new action with the given name and function
        self.actions[name] = Action(name, func)

    def get(self, name):
        """
        Retrieves an action by its name, allowing the agent to execute registered actions dynamically.
        """
        # Retrieve an action by its name
        return self.actions.get(name)
