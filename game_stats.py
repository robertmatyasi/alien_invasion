import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an inactive state.
        self.game_active = False

        # Load high score
        self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Saves high score into a file."""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)

    def load_high_score(self):
        """Loads high score from a file."""
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                self.saved_high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
        else:
            self.high_score = self.saved_high_score