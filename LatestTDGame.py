import pygame

# classes
class Enemy_Firebug(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.speed = 3
        self.path = path
        self.current_node = 0
        self.facing_direction = "right"

        # animation related
        self.enemy_firebug_sheet = pygame.image.load("spire_enemies_ground\Ground\Spritesheets\Firebug.png").convert_alpha()
        self.frame_counter = 16
        
        self.frames = [
            # bug facing up
            pygame.Rect((32, 256, 64, 64)),
            pygame.Rect((160, 256, 64, 64)),
            pygame.Rect((288, 256, 64, 64)),
            pygame.Rect((416, 256, 64, 64)),
            pygame.Rect((544, 256, 64, 64)),
            pygame.Rect((672, 256, 64, 64)),
            pygame.Rect((800, 256, 64, 64)),
            pygame.Rect((928, 256, 64, 64)),
            # bug facing down
            pygame.Rect((32, 192, 64, 64)),
            pygame.Rect((160, 192, 64, 64)),
            pygame.Rect((288, 192, 64, 64)),
            pygame.Rect((416, 192, 64, 64)),
            pygame.Rect((544, 192, 64, 64)),
            pygame.Rect((672, 192, 64, 64)),
            pygame.Rect((800, 192, 64, 64)),
            pygame.Rect((928, 192, 64, 64)),
            # bug facing sideways
            pygame.Rect((32, 320, 64, 64)),
            pygame.Rect((160, 320, 64, 64)),
            pygame.Rect((288, 320, 64, 64)),
            pygame.Rect((416, 320, 64, 64)),
            pygame.Rect((544, 320, 64, 64)),
            pygame.Rect((672, 320, 64, 64)),
            pygame.Rect((800, 320, 64, 64)),
            pygame.Rect((928, 320, 64, 64))
        ]

        self.image = pygame.Surface(self.frames[self.frame_counter].size, pygame.SRCALPHA).convert_alpha()
        self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[self.frame_counter])

        self.rect = self.image.get_rect(topleft = path[0])

    def animation_state(self):
        self.frame_counter += 0.5
        if self.facing_direction == "up":
            print("facing up")
            if int(self.frame_counter) > 7 or int(self.frame_counter) < 0: self.frame_counter = 0
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[int(self.frame_counter)])

        elif self.facing_direction == "down":
            print("facing down")
            if int(self.frame_counter) > 14 or int(self.frame_counter) < 8: self.frame_counter = 8
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[int(self.frame_counter)])
            
        elif self.facing_direction == "right":
            print("facing right")
            if int(self.frame_counter) > 23 or int(self.frame_counter) < 16: self.frame_counter = 16
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[int(self.frame_counter)])

        elif self.facing_direction == "left":
            print("facing left")
            if int(self.frame_counter) > 23 or int(self.frame_counter) < 16: self.frame_counter = 16
            self.image.fill((0,0,0,0))
            self.image.blit(self.enemy_firebug_sheet, (0, 0), self.frames[int(self.frame_counter)])
            self.temp_image_holder = pygame.transform.flip(self.image, True, False)
            self.image.fill((0,0,0,0))
            self.image.blit(self.temp_image_holder, (0,0))

    # used by position to move the enemy
    def moving_right(self):
        if self.rect.x >= self.next_node[0]:
            return False
        else:
            self.rect.x += self.speed
            return True
    def moving_left(self):
        if self.rect.x <= self.next_node[0]:
            return False
        else:
            self.rect.x -= self.speed
            return True
    def moving_up(self):
        if self.rect.y <= self.next_node[1]:
            return False
        else:
            self.rect.y -= self.speed
            return True
    def moving_down(self):
        if self.rect.y >= self.next_node[1]:
            return False
        else:
            self.rect.y += self.speed
            return True

    def position(self):
        if self.current_node >= len(self.path) - 1:
            quit()
        else:
            self.current_node_info = self.path[self.current_node]
            self.next_node = self.path[self.current_node + 1]

            if self.next_node[0] > self.current_node_info[0]:
                # move enemy to the right
                if self.moving_right():
                    print("moving right")
                    self.facing_direction = "right"
                else:
                    self.rect.x = self.next_node[0]
                    self.current_node += 1
            elif self.next_node[0] < self.current_node_info[0]:
                # move enemy to the left
                if self.moving_left():
                    print("moving left")
                    self.facing_direction = "left"
                else:
                    self.rect.x = self.next_node[0]
                    self.current_node += 1
            elif self.next_node[1] < self.current_node_info[1]:
                # move enemy up
                if self.moving_up():
                    print("moving up")
                    self.facing_direction = "up"
                else:
                    self.rect.y = self.next_node[1]
                    self.current_node += 1
            elif self.next_node[1] > self.current_node_info[1]:
                # move enemy down
                if self.moving_down():
                    print("moving down")
                    self.facing_direction = "down"
                else:
                    self.rect.y = self.next_node[1]
                    self.current_node += 1

    def update(self):
        self.animation_state()
        self.position()

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.level_1_tower_sheet = pygame.image.load("spire_towerpack\Towers Weapons\Tower 01\Spritesheets\Tower 01 - Level 01 - Weapon.png").convert_alpha()

        self.range = 100
        self.damage = 10
        self.attack_speed = 1.0
        self.last_attack_time = 0
        self.x = x
        self.y = y

        self.frame_counter = 0

        self.frames = [
            pygame.Rect((0, 0, 96, 96))
        ]

        self.image = pygame.Surface(self.frames[self.frame_counter].size, pygame.SRCALPHA).convert_alpha()
        # self.image.fill((0, 0, 0, 0))
        self.image.blit(self.level_1_tower_sheet, (0, 0), self.frames[self.frame_counter])
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def update(self, enemies):
        # Find the closest enemy within range
        closest_enemy = None
        closest_distance = self.range
        for enemy in enemies:
            distance = pygame.math.Vector2(enemy.rect.center).distance_to(pygame.math.Vector2(self.rect.center))
            if distance <= closest_distance:
                closest_enemy = enemy
                closest_distance = distance

        # If an enemy is in range, rotate the tower to face it
        if closest_enemy:
            direction = pygame.math.Vector2(closest_enemy.rect.center) - pygame.math.Vector2(self.rect.center)
            self.angle = direction.angle_to(pygame.math.Vector2(1, 0))
            self.image = pygame.transform.rotate(self.image, -self.angle)

        # # Check if it's time to attack
        # if current_time - self.last_attack_time > 1000 * self.attack_speed:
        #     self.last_attack_time = current_time

        #     # Look for an enemy within range
        #     target = None
        #     for enemy in enemies:
        #         distance = self.rect.centerx - enemy.rect.centerx
        #         if abs(distance) <= self.attack_range:
        #             if target is None or abs(distance) < abs(self.rect.centerx - target.rect.centerx):
        #                 target = enemy

        #     # Attack the target
        #     if target:
        #         target.health -= self.damage
        #         if target.health <= 0:
        #             enemies.remove(target)

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
path = [
    (-64,64), (384,64), (384,192), 
    (640,192), (640,64), (832,64), 
    (832,386), (192,384), (192,192),
    (64,192), (64,512), (960,512)
]

# initiating groups
enemies = pygame.sprite.Group()
enemies.add(Enemy_Firebug(path))

towers = pygame.sprite.Group()
towers.add(Tower(200, 200))

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button was clicked
            if event.button == 1:
                # Get the position of the mouse click
                mouse_x, mouse_y = event.pos
                # Do something with the mouse position
                towers.add(Tower(mouse_x, mouse_y))

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
    towers.draw(screen)
    towers.update(enemies)

    # Flip the display
    pygame.display.flip()

    # Set the game clock
    clock.tick(30)

# Clean up Pygame
pygame.quit()
