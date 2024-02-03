from abc import ABC, abstractmethod


# Step 1: Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element_b):
        pass

# Concrete Visitor A
class ConcreteVisitorA(Visitor):
    def visit_concrete_element_a(self, element_a):
        print(f"Visitor A visiting {element_a}")

    def visit_concrete_element_b(self, element_b):
        print(f"Visitor A visiting {element_b}")

# Concrete Visitor B
class ConcreteVisitorB(Visitor):
    def visit_concrete_element_a(self, element_a):
        print(f"Visitor B visiting: {element_a}")

    def visit_concrete_element_b(self, element_b):
        print(f"Visitor B visiting: {element_b}")

# Step 3: Element Interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

# Step 4: Concrete Elements
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "Operation A"
    
    def __str__(self):
        return "Concrete Element A"

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "Operation B"
    
    def __str__(self):
        return "Concrete Element B"

# Client Code
if __name__ == "__main__":
    # Creating concrete elements
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    # Creating concrete visitors
    visitor_a = ConcreteVisitorA()
    visitor_b = ConcreteVisitorB()

    # Accepting visitors
    element_a.accept(visitor_a)
    element_b.accept(visitor_a)

    element_a.accept(visitor_b)
    element_b.accept(visitor_b)