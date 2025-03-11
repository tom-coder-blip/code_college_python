import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet, Bomb
from alien import Alien
from difficulty_button import DifficultyButton


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()  # Add a group for bombs
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.game_paused = False  # Add a paused state

        # Make the Play button.
        self.play_button = Button(self, "Play")

        self.last_bomb_time = 0  # Track when the last bomb was dropped

        # Add difficulty selection state
        self.selecting_difficulty = False
        # Create difficulty buttons
        screen_center_x = self.settings.screen_width // 2
        screen_center_y = self.settings.screen_height // 2
        self.difficulty_buttons = {
            'Easy': DifficultyButton(self, "Easy", (screen_center_x, screen_center_y - 100)),
            'Medium': DifficultyButton(self, "Medium", (screen_center_x, screen_center_y)),
            'Hard': DifficultyButton(self, "Hard", (screen_center_x, screen_center_y + 100))
        }

        pygame.mixer.init()  # Initialize sound mixer

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Load sound effects
        self.bullet_sound = pygame.mixer.Sound("sounds/space_slash.mp3")
        self.bullet_sound.set_volume(0.3)  # Adjust volume (0.0 - 1.0)
        #self.ship_sound = pygame.mixer.Sound("sounds/space-animal-104986.mp3")
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.mp3")
        self.game_over_sound.set_volume(0.4)
        
        self.bomb_explosion_sound = pygame.mixer.Sound("sounds/bomb_explosion.mp3")  # Use your actual file
        self.bomb_explosion_sound.set_volume(0.6)  # Adjust volume if needed

        self.explosion_sound = pygame.mixer.Sound("sounds/alien_explosion.mp3") 
        self.explosion_sound.set_volume(0.2)  # Adjust volume if needed goes under 2nd if statement in your collisions function

        # Load and play background music (loop indefinitely)
        pygame.mixer.music.load("sounds/space_ambience.mp3")
        pygame.mixer.music.set_volume(0.2)  # Adjust volume (0.0 - 1.0)
        pygame.mixer.music.play(-1)  # Loop forever
  
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active and not self.game_paused:
                self.ship.update()
                self._update_bullets()
                self._update_bombs()  # Update bombs
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # Save high score before exiting
                self.stats.save_high_score(self.stats.high_score)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.selecting_difficulty:
                    self._check_play_button(mouse_pos)
                else:
                    self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start difficulty selection when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Only set selecting_difficulty to True, don't start the game yet
            self.selecting_difficulty = True
        
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
        
            # Keep mouse visible for difficulty selection
            pygame.mouse.set_visible(True)   

    def _check_difficulty_buttons(self, mouse_pos):
        """Check if a difficulty button was clicked."""
        if self.selecting_difficulty:
            for difficulty, button in self.difficulty_buttons.items():
                if button.rect.collidepoint(mouse_pos):
                    self.settings.set_difficulty(difficulty)
                    self._start_game()
    
    def _start_game(self):
        """Start the game with the selected difficulty."""
        self.selecting_difficulty = False
        self.game_active = True
        
        # Reset game state
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        
        # Clear the screen
        self.bullets.empty()
        self.bombs.empty()
        self.aliens.empty()
        
        # Create new fleet and center ship
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide mouse cursor during gameplay
        pygame.mouse.set_visible(False)
        
        # Create the timer
        self._create_timer()
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Save high score before quitting
            self.stats.save_high_score(self.stats.high_score)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_b:
            self._drop_bomb()
        elif event.key == pygame.K_p:
            self._toggle_pause()
        elif event.key == pygame.K_s:
            self.stats.game_active = True
            pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _toggle_pause(self):
        """Toggle the game's paused state."""
        self.game_paused = not self.game_paused
        if self.game_paused:
            self.pause_start_time = pygame.time.get_ticks()
        else:
            pause_duration = pygame.time.get_ticks() - self.pause_start_time
            self.start_time += pause_duration

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_sound.play()

    def _drop_bomb(self):
        """Create a new bomb if enough time has passed."""
        current_time = pygame.time.get_ticks()
        time_since_last_bomb = current_time - self.last_bomb_time
        
        if (time_since_last_bomb >= self.settings.bomb_recharge_time 
                and len(self.bombs) < self.settings.bombs_allowed 
                and self.game_active):
            new_bomb = Bomb(self)
            self.bombs.add(new_bomb)
            self.last_bomb_time = current_time
            print(f"Bomb dropped! Recharge in {self.settings.bomb_recharge_time/1000} seconds")
        else:
            remaining_time = (self.settings.bomb_recharge_time - time_since_last_bomb) / 1000
            if remaining_time > 0:
                print(f"Bomb recharging... {remaining_time:.1f} seconds remaining")

    def _draw_bomb_recharge(self):
        """Draw the bomb recharge indicator."""
        current_time = pygame.time.get_ticks()
        time_since_last_bomb = current_time - self.last_bomb_time
        recharge_progress = min(time_since_last_bomb / self.settings.bomb_recharge_time, 1.0)
        
        # Draw recharge indicator in bottom left corner
        indicator_width = 100
        indicator_height = 10
        x = 20
        y = self.settings.screen_height - 30
        
        # Draw background bar (red)
        pygame.draw.rect(self.screen, (255, 0, 0), 
                        (x, y, indicator_width, indicator_height))
        
        # Draw progress bar (green)
        progress_width = int(indicator_width * recharge_progress)
        if progress_width > 0:
            pygame.draw.rect(self.screen, (0, 255, 0),
                            (x, y, progress_width, indicator_height))

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_bombs(self):
        """Update position of bombs and check for collisions."""
        self.bombs.update()
    
        # Check for bomb-alien collisions
        self._check_bomb_alien_collisions()
    
        # Remove bombs that have gone off screen
        for bomb in self.bombs.copy():
            if bomb.rect.top >= self.settings.screen_height:
                self.bombs.remove(bomb)

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.explosion_sound.play()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_bomb_alien_collisions(self):
        """Respond to bomb-alien collisions with area effect."""
        # Check for direct collisions first
        bomb_alien_collisions = pygame.sprite.groupcollide(
            self.bombs, self.aliens, False, False)

        for bomb, aliens in bomb_alien_collisions.items():
            if not bomb.is_exploding:  # Only start explosion if not already exploding
                bomb.start_explosion()  # Start the explosion animation
                self.bomb_explosion_sound.play()  # Play bomb explosion sound

                # Get the explosion center point
                center_x = bomb.rect.centerx
                center_y = bomb.rect.centery

                # Check all aliens for distance to explosion
                for alien in self.aliens.sprites():
                    # Calculate distance between bomb and alien
                    distance = ((alien.rect.centerx - center_x) ** 2 + 
                       (alien.rect.centery - center_y) ** 2) ** 0.5

                    # If alien is within explosion radius, destroy it
                    if distance <= bomb.explosion_radius:
                        self.aliens.remove(alien)
                        self.stats.score += self.settings.alien_points

                self.sb.prep_score()
                self.sb.check_high_score()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets, bombs, and aliens.
            self.bullets.empty()
            self.bombs.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.game_over_sound.play

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_timer(self):
        """Create a timer to track the time elapsed in the game."""
        self.start_time = pygame.time.get_ticks()

    def _update_timer(self):
        """Update the timer and display the elapsed time in minutes and seconds."""
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        time_str = f"{minutes:02}:{seconds:02}"
        self.sb.prep_time(time_str)

    def _draw_paused_text(self):
        """Draw the 'Paused' text on the screen."""
        font = pygame.font.SysFont(None, 48)
        paused_text = font.render("Paused", True, (255, 0, 0))
        paused_rect = paused_text.get_rect()
        paused_rect.center = self.screen.get_rect().center
        self.screen.blit(paused_text, paused_rect)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        if self.game_active:
            for bomb in self.bombs.sprites():
                bomb.draw_bomb()
                # Add a debug rectangle to verify position
                pygame.draw.rect(self.screen, (0, 255, 0), bomb.rect, 1)  # Green outline
            
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            
            self.ship.blitme()
            self.aliens.draw(self.screen)
            # Draw the score information.
            self.sb.show_score()
            # Update and draw the timer.
            self._update_timer()
             # Draw the bomb recharge indicator
            self._draw_bomb_recharge()
            if self.game_paused:
                self._draw_paused_text()
        elif self.selecting_difficulty:
            # Draw difficulty buttons
            for button in self.difficulty_buttons.values():
                button.draw_button()
        else:
            # Draw the play button if the game is inactive.
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()