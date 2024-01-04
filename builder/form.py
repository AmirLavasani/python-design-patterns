from abc import ABC, abstractmethod

class Builder(ABC):
    """Abstract Builder Interface for constructing forms."""
    
    @abstractmethod
    def add_name_field(self):
        pass
    
    @abstractmethod
    def add_email_field(self):
        pass
    
    @abstractmethod
    def add_subscribe_field(self):
        pass
    
    @abstractmethod
    def build(self):
        pass

class FormField:
    """Represents a form field with a label and input type."""

    def __init__(self, label, input_type):
        self.label = label
        self.input_type = input_type

    def __str__(self):
        return f"{self.label}: <input type='{self.input_type}'>"


class FormBuilderDirector:
    """Director for constructing complex forms using a specific builder."""

    def __init__(self, builder):
        self.builder = builder

    def construct_form(self):
        """Construct the form using the builder."""
        self.builder.add_name_field().add_email_field().add_subscribe_field()


class FormBuilder(Builder):
    """Concrete Builder for constructing forms."""

    def __init__(self):
        self.form = []

    def add_name_field(self):
        """Add a name field to the form."""
        self.form.append(FormField("Name", "text"))
        return self

    def add_email_field(self):
        """Add an email field to the form."""
        self.form.append(FormField("Email", "email"))
        return self

    def add_subscribe_field(self):
        """Add a subscribe checkbox to the form."""
        self.form.append(FormField("Subscribe", "checkbox"))
        return self

    def build(self):
        """Build the form.

        Returns:
            str: The HTML representation of the form.
        """
        form = "\n".join(str(field) for field in self.form)
        return f"<form>\n{form}\n</form>"


if __name__ == "__main__":
    # Demonstrate form generation using the Builder Pattern
    builder = FormBuilder()
    director = FormBuilderDirector(builder)
    director.construct_form()
    form = builder.build()

    print("Generated Form:")
    print(form)
