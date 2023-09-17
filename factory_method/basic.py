from abc import ABC, abstractmethod


class Localizer(ABC):
    """
    Abstract Product: Represents translations for specific languages.
    
    This is an abstract class defining the interface for concrete localizers.
    """
    
    @abstractmethod
    def localize(self, msg):
        """
        Translate the given message.
        
        Args:
            msg (str): The message to be translated.
            
        Returns:
            str: The translated message.
        """
        pass


class FrenchLocalizer(Localizer):
    """
    Concrete Product: Represents translations for French.
    
    This class provides translations for French language.
    """
    
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        """
        Translate the message to French.
        
        Args:
            msg (str): The message to be translated.
            
        Returns:
            str: The translated message.
        
        Example:
            >>> localizer = FrenchLocalizer()
            >>> localizer.localize("car")
            'voiture'
        """
        return self.translations.get(msg, msg)


class SpanishLocalizer(Localizer):
    """
    Concrete Product: Represents translations for Spanish.
    
    This class provides translations for Spanish language.
    """
    
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg):
        """
        Translate the message to Spanish.
        
        Args:
            msg (str): The message to be translated.
            
        Returns:
            str: The translated message.
        
        Example:
            >>> localizer = SpanishLocalizer()
            >>> localizer.localize("bike")
            'bicicleta'
        """
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    """
    Concrete Product: Represents translations for English.
    
    This class provides translations for the English language.
    """
    
    def localize(self, msg):
        """
        Return the message as is (no translation).
        
        Args:
            msg (str): The message to be translated.
            
        Returns:
            str: The same message.
        
        Example:
            >>> localizer = EnglishLocalizer()
            >>> localizer.localize("cycle")
            'cycle'
        """
        return msg


class LocalizerFactory(ABC):
    """
    Abstract Creator: Defines the Factory Method to create localizers.
    
    This is an abstract class defining the interface for concrete localizer factories.
    """
    
    @abstractmethod
    def create_localizer(self):
        """
        Factory Method: Create a Localizer instance.
        
        Returns:
            Localizer: An instance of a concrete Localizer.
        """
        pass


class FrenchLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates FrenchLocalizer instances.
    
    This class creates FrenchLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        """
        Factory Method implementation for creating FrenchLocalizer.
        
        Returns:
            FrenchLocalizer: An instance of FrenchLocalizer.
        
        Example:
            >>> factory = FrenchLocalizerFactory()
            >>> localizer = factory.create_localizer()
            >>> localizer.localize("car")
            'voiture'
        """
        return FrenchLocalizer()


class SpanishLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates SpanishLocalizer instances.
    
    This class creates SpanishLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        """
        Factory Method implementation for creating SpanishLocalizer.
        
        Returns:
            SpanishLocalizer: An instance of SpanishLocalizer.
        
        Example:
            >>> factory = SpanishLocalizerFactory()
            >>> localizer = factory.create_localizer()
            >>> localizer.localize("bike")
            'bicicleta'
        """
        return SpanishLocalizer()


class EnglishLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates EnglishLocalizer instances.
    
    This class creates EnglishLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        """
        Factory Method implementation for creating EnglishLocalizer.
        
        Returns:
            EnglishLocalizer: An instance of EnglishLocalizer.
        
        Example:
            >>> factory = EnglishLocalizerFactory()
            >>> localizer = factory.create_localizer()
            >>> localizer.localize("cycle")
            'cycle'
        """
        return EnglishLocalizer()


def main():
    # Create Factory instances for different languages
    french_factory = FrenchLocalizerFactory()
    english_factory = EnglishLocalizerFactory()
    spanish_factory = SpanishLocalizerFactory()

    message = ["car", "bike", "cycle"]

    # Create and use localizers without knowing the concrete classes
    french_localizer = french_factory.create_localizer()
    english_localizer = english_factory.create_localizer()
    spanish_localizer = spanish_factory.create_localizer()

    for msg in message:
        # Translate and print the messages
        print(f"Message: {msg}")
        print(f"French: {french_localizer.localize(msg)}")
        print(f"English: {english_localizer.localize(msg)}")
        print(f"Spanish: {spanish_localizer.localize(msg)}")
        print("-" * 30)


if __name__ == "__main__":
    main()  # Run the main function
