class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.set_difficulty('easy')

        self.initialize_dynamic_settings()
    
    def set_difficulty(self, difficulty):
        """Game difficulty"""
        # How quickly the game speeds up and game speed multiplier
        if difficulty == 'easy':
            print('easy')
            self.speedup_scale = 1.1
            self.diff_multiplier = 1
        elif difficulty == 'medium':
            print('medium')
            self.speedup_scale = 1.2
            self.diff_multiplier = 1.3
        elif difficulty == 'hard':
            print('hard')
            self.speedup_scale = 1.3
            self.diff_multiplier = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5 * self.diff_multiplier
        self.bullet_speed = 1.5 * self.diff_multiplier
        self.alien_speed = 1.0 * self.diff_multiplier

        # Scoring
        self.alien_points = round(50 * self.diff_multiplier)

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)