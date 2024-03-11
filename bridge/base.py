from abc import ABC, abstractmethod

# Step 1: Define Abstraction (Abstract class)
class Abstraction(ABC):
    """Abstract class representing the high-level control layer."""
    
    def __init__(self, implementation):
        self._implementation = implementation

    @abstractmethod
    def perform_action(self):
        """Perform an action using the implementation."""
        pass

# Step 2: Define Implementation (Abstract class)
class Implementation(ABC):
    """Abstract class representing the platform-specific code."""
    
    @abstractmethod
    def action_impl(self):
        """Perform the actual action."""
        pass

# Step 3: Create Concrete Implementations
class ConcreteImplementationA(Implementation):
    """Concrete implementation for platform A."""
    
    def action_impl(self):
        return "Action performed by Implementation A"

class ConcreteImplementationB(Implementation):
    """Concrete implementation for platform B."""
    
    def action_impl(self):
        return "Action performed by Implementation B"

# Step 4: Create Refined Abstractions
class RefinedAbstraction(Abstraction):
    """Refined abstraction providing variants of control logic."""
    
    def perform_action(self):
        """Perform an action using the implementation."""
        return self._implementation.action_impl()

# Main section to showcase usage
if __name__ == "__main__":
    # Create concrete implementations
    implementation_a = ConcreteImplementationA()
    implementation_b = ConcreteImplementationB()

    # Create refined abstractions and link them with concrete implementations
    refined_abstraction_a = RefinedAbstraction(implementation_a)
    refined_abstraction_b = RefinedAbstraction(implementation_b)

    # Use refined abstractions to perform actions
    print(refined_abstraction_a.perform_action())  # Output: Action performed by Implementation A
    print(refined_abstraction_b.perform_action())  # Output: Action performed by Implementation B