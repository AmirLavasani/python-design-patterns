from abc import ABC, abstractmethod

# Step 1: Create the Strategy Interface
class Strategy(ABC):
    @abstractmethod
    def execute_strategy(self):
        pass

# Step 2: Create Concrete Strategies
class ConcreteStrategyA(Strategy):
    def execute_strategy(self):
        return "Executing Strategy A"

class ConcreteStrategyB(Strategy):
    def execute_strategy(self):
        return "Executing Strategy B"

# Step 3: Create the Context
class Context:
    def __init__(self, strategy):
        # Step 4: Context maintains a reference to one of the concrete strategies
        self._strategy = strategy

    def set_strategy(self, strategy):
        # Exposes a setter to replace the strategy associated with the context at runtime
        self._strategy = strategy

    def execute_strategy(self):
        # Step 5: Context calls the execution method on the linked strategy object
        return self._strategy.execute_strategy()

# Main Section to Showcase Usage
if __name__ == "__main__":
    # Create concrete strategy objects
    strategy_a = ConcreteStrategyA()
    strategy_b = ConcreteStrategyB()

    # Create context with a default strategy
    context = Context(strategy_a)

    # Execute the default strategy
    print(context.execute_strategy())  # Output: Executing Strategy A

    # Switch to a different strategy at runtime
    context.set_strategy(strategy_b)
    print(context.execute_strategy())  # Output: Executing Strategy B
