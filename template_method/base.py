from abc import ABC, abstractmethod

# Step 1: Abstract Class (Template)
class AbstractTemplate(ABC):
    def template_method(self):
        """The template method orchestrating the steps."""
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        """Abstract method representing the first step."""
        pass

    @abstractmethod
    def step_two(self):
        """Abstract method representing the second step."""
        pass

    @abstractmethod
    def step_three(self):
        """Abstract method representing the third step."""
        pass

# Step 2: Concrete Class 1
class ConcreteTemplateA(AbstractTemplate):
    def step_one(self):
        """Concrete implementation for the first step in Template A."""
        print("Performing step one for Template A.")

    def step_two(self):
        """Concrete implementation for the second step in Template A."""
        print("Performing step two for Template A.")

    def step_three(self):
        """Concrete implementation for the third step in Template A."""
        print("Performing step three for Template A.")

# Step 3: Concrete Class 2
class ConcreteTemplateB(AbstractTemplate):
    def step_one(self):
        """Concrete implementation for the first step in Template B."""
        print("Performing step one for Template B.")

    def step_two(self):
        """Concrete implementation for the second step in Template B."""
        print("Performing step two for Template B.")

    def step_three(self):
        """Concrete implementation for the third step in Template B."""
        print("Performing step three for Template B.")

# Main Section
if __name__ == "__main__":
    # Creating instances of concrete classes
    template_a = ConcreteTemplateA()
    template_b = ConcreteTemplateB()

    # Using the template method to perform steps
    print("Executing Template A:")
    template_a.template_method()

    print("\nExecuting Template B:")
    template_b.template_method()