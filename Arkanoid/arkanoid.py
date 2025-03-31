import pygame
import random
import datetime

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()

# Cargar sonidos
pygame.mixer.init()
sound_bounce = pygame.mixer.Sound("Arkanoid/bounce.wav")
sound_block = pygame.mixer.Sound("Arkanoid/block_hit.wav")
sound_gameover = pygame.mixer.Sound("Arkanoid/gameover.wav")

# Clase para la pala
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# Clase para la bola
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.vx, self.vy = 4, -4

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx = -self.vx
            sound_bounce.play()
        if self.rect.top <= 0:
            self.vy = -self.vy
            sound_bounce.play()
        
# Clase para los bloques
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))

# Grupos de sprites
all_sprites = pygame.sprite.Group()
paddle = Paddle()
ball = Ball()
blocks = pygame.sprite.Group()

all_sprites.add(paddle, ball)

for i in range(8):
    for j in range(5):
        block = Block(100 + i * 70, 50 + j * 30)
        blocks.add(block)
        all_sprites.add(block)

# Bucle del juego
running = True
while running:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    # Colisión de la bola con la pala
    if pygame.sprite.collide_rect(ball, paddle):
        ball.vy = -ball.vy
        sound_bounce.play()
    
    # Colisión de la bola con los bloques
    hit_blocks = pygame.sprite.spritecollide(ball, blocks, True)
    if hit_blocks:
        ball.vy = -ball.vy
        sound_block.play()
    
    # Si la bola cae por debajo de la pantalla
    if ball.rect.top > HEIGHT:
        sound_gameover.play()
        pygame.time.delay(5000)
        running = False
    
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()