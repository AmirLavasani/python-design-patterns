# Step 1: Define the State Interface
class State:
    """Interface defining the methods for various states."""
    def handle_state(self):
        """Abstract method to handle state behavior."""
        pass

# Step 2: Create Concrete State Classes
class ConcreteStateA(State):
    """Concrete state representing State A."""
    def handle_state(self):
        """Handle State A behavior."""
        print("Handling State A behavior.")

class ConcreteStateB(State):
    """Concrete state representing State B."""
    def handle_state(self):
        """Handle State B behavior."""
        print("Handling State B behavior.")

class ConcreteStateC(State):
    """Concrete state representing State C."""
    def handle_state(self):
        """Handle State C behavior."""
        print("Handling State C behavior.")

# Step 3: Create the Context Class
class Context:
    """Context class managing the states."""
    def __init__(self, state):
        """Initialize with a state."""
        self._state = state

    def change_state(self, state):
        """Change the current state."""
        self._state = state

    def request_state_action(self):
        """Perform an action based on the current state."""
        self._state.handle_state()

# Step 4: Example of Usage
if __name__ == "__main__":
    # Create instances of different states
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()
    state_c = ConcreteStateC()

    # Initialize the context with State A
    context = Context(state_a)
    context.request_state_action()  # Output: Handling State A behavior.

    # Change the state to State B
    context.change_state(state_b)
    context.request_state_action()  # Output: Handling State B behavior.

    # Change the state to State C
    context.change_state(state_c)
    context.request_state_action()  # Output: Handling State C behavior.
