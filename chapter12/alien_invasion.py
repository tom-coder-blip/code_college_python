import sys
import pygame
from settings import Settings
from ship import Ship  # Import the Ship class

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # Create game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance of Ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() # Handle user input (keyboard/mouse)
            self._update_screen() # Update the screen

            # Limit frame rate to 60 FPS
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)  # Fill background color
        self.ship.blitme()  # Draw the ship

        pygame.display.flip()  # Update the display

# Run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()