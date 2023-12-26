from abc import ABC, abstractmethod

# Step 1: Component - The base game character
class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

# Step 2: Concrete Component - Basic game character
class BasicCharacter(Character):
    def __init__(self):
        self.damage = 10
        self.armor = 5

    def attack(self):
        return f"(Damage: {self.damage})"

    def defend(self):
        return f"(Armor: {self.armor})"

# Step 3: Decorator - Abstract decorator class
class CharacterDecorator(Character):
    def __init__(self, character):
        self.damage = character.damage
        self.armor = character.armor
        self._character = character

    def attack(self):
        return self._character.attack()

    def defend(self):
        return self._character.defend()

# Step 4: Concrete Decorator - Double Damage decorator
class DoubleDamageDecorator(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        self._character.damage += 10

    def attack(self):
        return f"Double Damage! {self._character.attack()}"

# Step 4: Concrete Decorator - Fireball decorator
class FireballDecorator(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        self._character.damage += 5

    def attack(self):
        return f"Fireball! {self._character.attack()}"

# Step 4: Concrete Decorator - Invisibility decorator
class InvisibilityDecorator(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
        self._character.armor += 5

    def defend(self):
        return f"Invisible Defense! {self._character.defend()}"

# Step 5: Client Code - Creating a character with abilities
basic_character = BasicCharacter()
character_with_double_damage = DoubleDamageDecorator(BasicCharacter())
character_with_invisibility = InvisibilityDecorator(BasicCharacter())

def display_ability_info(character, ability_name):
    print(f"{ability_name}")
    print(f"Damage: {character.attack()}")
    print(f"Armor: {character.defend()}")
    print(f"{'*'*10}")

# Basic Character
display_ability_info(basic_character, "Basic")

# Character with Double Damage
display_ability_info(character_with_double_damage, "Double Damage")

# Character with Invisibility
display_ability_info(character_with_invisibility, "Invisibility")

# Create a special character with Double Damage and Invisibility
special_character = InvisibilityDecorator(character_with_double_damage)

# Special Character with Double Damage and Invisibility
display_ability_info(special_character, "Special Character (Double Damage and Invisibility)")

# Create a special character with Double Damage and Invisibility
special_character_2 = DoubleDamageDecorator(DoubleDamageDecorator(BasicCharacter()))

# Special Character with Double Damage and Invisibility
display_ability_info(special_character_2, "Special Character (Double Damage and Invisibility)")