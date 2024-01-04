from abc import ABC, abstractmethod


class Director:
    """The Director class orchestrates the object construction process."""

    def construct(self, builder):
        """Constructs the complex object using the given builder."""
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()


class Builder(ABC):
    """The Builder interface declares methods for building different parts of the complex object."""

    @abstractmethod
    def build_part_a(self):
        """Abstract method to build Part A."""
        pass

    @abstractmethod
    def build_part_b(self):
        """Abstract method to build Part B."""
        pass

    @abstractmethod
    def build_part_c(self):
        """Abstract method to build Part C."""
        pass


class ConcreteBuilderA(Builder):
    """The ConcreteBuilderA class provides specific implementations for building parts of the complex object."""

    def __init__(self):
        """Initialize the ConcreteBuilderA instance."""
        self.product = Product()

    def build_part_a(self):
        """Build Part A specific to ConcreteBuilderA."""
        self.product.add("Part A1")

    def build_part_b(self):
        """Build Part B specific to ConcreteBuilderA."""
        self.product.add("Part B1")

    def build_part_c(self):
        """Build Part C specific to ConcreteBuilderA."""
        self.product.add("Part C1")


class ConcreteBuilderB(Builder):
    """The ConcreteBuilderB class provides specific implementations for building parts of the complex object."""

    def __init__(self):
        """Initialize the ConcreteBuilderB instance."""
        self.product = Product()

    def build_part_a(self):
        """Build Part A specific to ConcreteBuilderB."""
        self.product.add("Part A2")

    def build_part_b(self):
        """Build Part B specific to ConcreteBuilderB."""
        self.product.add("Part B2")

    def build_part_c(self):
        """Build Part C specific to ConcreteBuilderB."""
        self.product.add("Part C2")


class Product:
    """The Product class represents the complex object being built."""

    def __init__(self):
        """Initialize the Product instance."""
        self.parts = []

    def add(self, part):
        """Add a part to the product."""
        self.parts.append(part)


class Client:
    """The Client class creates and assembles products using builders."""

    def construct_product(self, builder):
        """Constructs the product using the provided builder."""
        director = Director()
        director.construct(builder)
        return builder.product


# Main section to build products with different builders
if __name__ == "__main__":
    client = Client()

    builder_a = ConcreteBuilderA()
    product_a = client.construct_product(builder_a)
    print("Product built by ConcreteBuilderA:")
    for part in product_a.parts:
        print(part)

    builder_b = ConcreteBuilderB()
    product_b = client.construct_product(builder_b)
    print("Product built by ConcreteBuilderB:")
    for part in product_b.parts:
        print(part)