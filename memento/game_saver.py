class Game:
    def __init__(self):
        self._state = None
        # Adding GameLevel attribute for state change demonstration
        self._level = 1

    def play(self):
        # Simulate game progress by increasing the game level
        self._level += 1
        print(f"Advanced to level {self._level}")

    def create_memento(self):
        # Storing the current game level as part of the state
        return GameState({"level": self._level})

    def restore(self, memento):
        self._state = memento.get_state()
        # Retrieving the stored game level
        self._level = self._state.get("level", 1)


class GameState:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state
    

class GameSaver:
    def __init__(self):
        self._saves = {}

    def save_game(self, name, state):
        self._saves[name] = state

    def load_game(self, name):
        return self._saves[name]


if __name__ == "__main__":
    # Instantiate classes
    game = Game()
    game_saver = GameSaver()

    # Play the game and save state
    game.play()
    saved_state = game.create_memento()
    game_saver.save_game("save_1", saved_state)

    # Advance game further
    game.play()

    # Load and restore saved state
    loaded_state = game_saver.load_game("save_1")
    game.restore(loaded_state)

    # Check restored state
    print(f"Restored to level {game._level}")