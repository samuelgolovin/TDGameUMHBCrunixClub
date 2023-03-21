import pygame
import math
# import TDGame_Classes.enemy_firebug_class

# classes
class Enemy_Firebug(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.speed = 3
        self.path = path
        self.current_node = 0
        self.facing_direction = "up"

        # animation related
        self.enemy_firebug_sheet = pygame.image.load("spire_enemies_ground\Ground\Spritesheets\Firebug.png").convert_alpha()
        self.frame_counter = 0
        
        self.frames = [
            # bug walking up
            pygame.Rect((32, 256, 64, 64)),
            pygame.Rect((160, 256, 64, 64)),
            pygame.Rect((288, 256, 64, 64)),
            pygame.Rect((416, 256, 64, 64)),
            pygame.Rect((544, 256, 64, 64)),
            pygame.Rect((672, 256, 64, 64)),
            pygame.Rect((800, 256, 64, 64)),
            pygame.Rect((928, 256, 64, 64)),
            # bug walking sideways
            pygame.Rect((0, 320, 128, 64)),
            pygame.Rect((128, 320, 128, 64)),
            pygame.Rect((256, 320, 128, 64)),
            pygame.Rect((384, 320, 128, 64)),
            pygame.Rect((512, 320, 128, 64)),
            pygame.Rect((640, 320, 128, 64)),
            pygame.Rect((768, 320, 128, 64)),
            pygame.Rect((896, 320, 128, 64))
        ]

        self.image = pygame.Surface(self.frames[self.frame_counter].size, pygame.SRCALPHA).convert_alpha()
        self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[self.frame_counter])
        

        self.rect = self.image.get_rect(midbottom = path[0])

    def animation_state(self):
        self.frame_counter += 0.12
        if self.facing_direction == "up" and self.frame_counter >= 0 or self.frame_counter <= 7:
            frame_index = int(self.frame_counter % len(self.frames))
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[frame_index])
            if self.frame_counter > 7: self.frame_counter = 0
        elif self.facing_direction == "left" and self.frame_counter >= 8 or self.frame_counter <= 14:
            frame_index = int(self.frame_counter % len(self.frames))
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[frame_index])
            if self.frame_counter > 14: self.frame_counter = 8

    def position(self):
        self.next_node = self.path[self.current_node + 1]
        if self.rect.x <= self.next_node[0]:
            self.rect.x += self.speed
            print(self.rect.x)

    def update(self):
        self.animation_state()
        self.position()


# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 960
window_height = 640
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tower Defense Game")

# Set up the game clock
clock = pygame.time.Clock()

# load images
background_image = pygame.image.load("maps/basic_map.png")

# Set the font for the text
font = pygame.font.SysFont('Arial', 20)

# set path of firebugs
path = [(-64,128), (384,128), (416,256), (672,256), (672,128), (864,128)]
test_path = [(400,400), (450,400)]

# initiating groups
enemies = pygame.sprite.Group()
enemies.add(Enemy_Firebug(path))

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update game logic

    # Render the game
    screen.blit(background_image, (0,0))
    # Get the position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Draw the text showing the mouse coordinates
    text_surface = font.render(f"Mouse coordinates: {mouse_pos}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))
    enemies.draw(screen)
    enemies.update()

    # Flip the display
    pygame.display.flip()

    # Set the game clock
    clock.tick(30)

# Clean up Pygame
pygame.quit()
