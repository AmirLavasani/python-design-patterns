from abc import ABC, abstractmethod
import random

# Step 1: Define the Flyweight interface
class EnemyFlyweight(ABC):
    """
    Flyweight interface declares a method for accepting extrinsic state
    and performing operations based on it.
    """

    @abstractmethod
    def render(self, position):
        """
        Render method accepting extrinsic state as input.
        """
        pass

# Step 2: Create concrete flyweight classes
class EnemyTypeA(EnemyFlyweight):
    """
    ConcreteFlyweight class for enemy type A.
    """

    def __init__(self, texture):
        self._texture = texture

    def render(self, position):
        """
        Render enemy type A with given position.
        """
        print(f"Rendering Enemy Type A at position {position} with texture: {self._texture}")

class EnemyTypeB(EnemyFlyweight):
    """
    ConcreteFlyweight class for enemy type B.
    """

    def __init__(self, texture):
        self._texture = texture

    def render(self, position):
        """
        Render enemy type B with given position.
        """
        print(f"Rendering Enemy Type B at position {position} with texture: {self._texture}")

# Step 3: Implement the Flyweight Factory
class EnemyFlyweightFactory:
    """
    FlyweightFactory manages flyweight objects and ensures their uniqueness.
    """

    _flyweights = {}

    @staticmethod
    def get_flyweight(texture):
        """
        Retrieve or create a flyweight object based on the provided texture.
        """
        if texture not in EnemyFlyweightFactory._flyweights:
            if random.randint(0, 1) == 0:
                EnemyFlyweightFactory._flyweights[texture] = EnemyTypeA(texture)
            else:
                EnemyFlyweightFactory._flyweights[texture] = EnemyTypeB(texture)
        return EnemyFlyweightFactory._flyweights[texture]

# Step 4: Define the client class
class GameEnvironment:
    """
    Client class represents objects that use flyweight objects.
    """

    def __init__(self):
        self._enemies = []

    def add_enemy(self, texture, position):
        """
        Add a new enemy to the game environment.
        """
        flyweight = EnemyFlyweightFactory.get_flyweight(texture)
        self._enemies.append((flyweight, position))

    def render_enemies(self):
        """
        Render all enemies in the game environment.
        """
        for flyweight, position in self._enemies:
            flyweight.render(position)

# Example usage
if __name__ == "__main__":
    # Create game environment
    game = GameEnvironment()

    # Add enemies with different textures and positions
    game.add_enemy("texture_a", (10, 20))
    game.add_enemy("texture_b", (30, 40))
    game.add_enemy("texture_a", (50, 60))
    game.add_enemy("texture_b", (70, 80))

    # Render all enemies
    game.render_enemies()
