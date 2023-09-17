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


def create_localizer(language="English"):
    """
    Factory Method: Create a localizer for the specified language.

    Args:
        language (str): The language for which to create a localizer.

    Returns:
        Localizer: An instance of the localizer for the specified language.

    Example:
        >>> french_localizer = create_localizer("French")
        >>> french_localizer.localize("car")
        'voiture'
        
        >>> english_localizer = create_localizer("English")
        >>> english_localizer.localize("bike")
        'bike'
        
        >>> spanish_localizer = create_localizer("Spanish")
        >>> spanish_localizer.localize("cycle")
        'ciclo'
    """
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()


def main():
    # Create localizers for different languages
    french_localizer = create_localizer("French")
    english_localizer = create_localizer("English")
    spanish_localizer = create_localizer("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        # Translate and print the messages
        print(f"Message: {msg}")
        print(f"French: {french_localizer.localize(msg)}")
        print(f"English: {english_localizer.localize(msg)}")
        print(f"Spanish: {spanish_localizer.localize(msg)}")
        print("-" * 30)

if __name__ == "__main__":
    main()  # Run the main function