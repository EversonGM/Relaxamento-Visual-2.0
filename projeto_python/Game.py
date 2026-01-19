import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Relaxamento dos Olhos - Siga a Bolinha")

# Cores
black = (0, 0, 0)
white = (255, 255, 255)

# Configurações da bolinha
radius = 20
x = width // 2
y = height // 2
speed = 5  # Velocidade de movimento

# Pede ao usuário a direção inicial
direction = input("Escolha a direção (left, right, up, down) ou 'random' para aleatório: ").lower()

# Define a velocidade inicial baseada na escolha
if direction == 'left':
    dx, dy = -speed, 0
elif direction == 'right':
    dx, dy = speed, 0
elif direction == 'up':
    dx, dy = 0, -speed
elif direction == 'down':
    dx, dy = 0, speed
elif direction == 'random':
    dx = random.choice([-speed, speed])
    dy = random.choice([-speed, speed])
    if dx == 0 and dy == 0:  # Evita ficar parada
        dx = speed
else:
    print("Direção inválida. Usando 'random'.")
    dx = random.choice([-speed, speed])
    dy = random.choice([-speed, speed])
    if dx == 0 and dy == 0:
        dx = speed

# Relógio para controlar FPS
clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a posição da bolinha
    x += dx
    y += dy

    # Verifica colisão com as bordas e quica (inverte direção)
    if x <= radius or x >= width - radius:
        dx = -dx
        # No modo random, muda direção de forma aleatória ao bater
        if direction == 'random':
            dx = random.choice([-speed, speed, 0])
            dy = random.choice([-speed, speed, 0])
            if dx == 0 and dy == 0:
                dx = speed

    if y <= radius or y >= height - radius:
        dy = -dy
        if direction == 'random':
            dx = random.choice([-speed, speed, 0])
            dy = random.choice([-speed, speed, 0])
            if dx == 0 and dy == 0:
                dx = speed

    # Preenche a tela de preto
    screen.fill(black)

    # Desenha a bolinha branca
    pygame.draw.circle(screen, white, (int(x), int(y)), radius)

    # Atualiza a tela
    pygame.display.flip()

    # Limita a 60 frames por segundo para movimento suave
    clock.tick(60)

# Finaliza o Pygame
pygame.quit()
sys.exit()


