from abc import ABC, abstractmethod

class Handler(ABC):
    """An abstract class for handling requests."""
    
    @abstractmethod
    def handle_request(self, request):
        """Handle the request."""
        pass

class ConcreteHandlerA(Handler):
    """A concrete handler that handles requests of type 'A'."""
    
    def handle_request(self, request):
        if request == 'A':
            print("Handled by Handler A")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    """A concrete handler that handles requests of type 'B'."""
    
    def handle_request(self, request):
        if request == 'B':
            print("Handled by Handler B")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)

class Chain:
    """A chain of handlers to process requests."""
    
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        """Add a handler to the chain."""
        self.handlers.append(handler)

    def handle_request(self, request):
        """Handle a request using the chain of handlers."""
        for handler in self.handlers:
            handler.handle_request(request)

if __name__ == "__main__":
    # Create a chain of handlers
    chain = Chain()
    chain.add_handler(ConcreteHandlerA())
    chain.add_handler(ConcreteHandlerB())

    # Test requests
    requests = ['A', 'B', 'C']

    for request in requests:
        print(f"Processing request: {request}")
        chain.handle_request(request)
