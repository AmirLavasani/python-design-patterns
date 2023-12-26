class Subsystem1:
    def operation1(self):
        """Subsystem1 operation"""
        return "Subsystem1: Ready!"

class Subsystem2:
    def operation2(self):
        """Subsystem2 operation"""
        return "Subsystem2: Ready!"

class Facade:
    def __init__(self):
        """Initialize subsystem objects"""
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        """Facade operation: coordinating subsystems"""
        result = []
        result.append(self._subsystem1.operation1())
        result.append(self._subsystem2.operation2())
        return '\n'.join(result)

def client_code(facade):
    """Client code utilizing the facade"""
    print(facade.operation())

# Usage
if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
