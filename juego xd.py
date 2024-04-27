import pygame
import random
import math
from pygame.locals import *

# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Parámetros de generación de terreno
TERRAIN_WIDTH = 1600
TERRAIN_HEIGHT = 1200
CELL_SIZE = 5
SCALE = 0.01

# Parámetros del desierto
SAND_COLOR = (194, 178, 128)
ROCK_COLOR = (119, 136, 153)

# Parámetros del jugador
PLAYER_SPEED = 2
PLAYER_ROTATION_SPEED = 2

# Inicializar Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Generador de Terreno - Desierto")

# Generar terreno
def generate_terrain():
    terrain = []
    for i in range(TERRAIN_WIDTH // CELL_SIZE):
        column = []
        for j in range(TERRAIN_HEIGHT // CELL_SIZE):
            noise_value = generate_noise(i * SCALE, j * SCALE)
            column.append(noise_value)
        terrain.append(column)
    return terrain

# Generar valor de ruido
def generate_noise(x, y):
    return random.uniform(0, 1)

# Dibujar terreno
def draw_terrain(terrain):
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            color = get_cell_color(terrain[i][j])
            pygame.draw.rect(window, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Obtener color de celda según altura
def get_cell_color(height):
    if height < 0.4:
        return SAND_COLOR
    else:
        return ROCK_COLOR

# Bucle principal del juego
def main():
    clock = pygame.time.Clock()
    terrain = generate_terrain()

    player_x = TERRAIN_WIDTH // 2
    player_y = TERRAIN_HEIGHT // 2
    player_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            player_x += math.cos(math.radians(player_angle)) * PLAYER_SPEED
            player_y -= math.sin(math.radians(player_angle)) * PLAYER_SPEED
        if keys[K_DOWN]:
            player_x -= math.cos(math.radians(player_angle)) * PLAYER_SPEED
            player_y += math.sin(math.radians(player_angle)) * PLAYER_SPEED
        if keys[K_LEFT]:
            player_angle = (player_angle + PLAYER_ROTATION_SPEED) % 360
        if keys[K_RIGHT]:
            player_angle = (player_angle - PLAYER_ROTATION_SPEED) % 360

        window.fill(SAND_COLOR)  # Color de fondo del desierto

        # Calcular el campo de visión del jugador
        fov = 60
        num_rays = WINDOW_WIDTH
        ray_angle = player_angle - fov / 2
        ray_angle_increment = fov / num_rays

        for ray in range(num_rays):
            distance_to_wall = 0
            hit_wall = False
            hit_boundary = False

            eye_x = math.cos(math.radians(ray_angle))
            eye_y = math.sin(math.radians(ray_angle))

            while not hit_wall and distance_to_wall < TERRAIN_WIDTH:
                distance_to_wall += 0.1

                test_x = int(player_x + eye_x * distance_to_wall)
                test_y = int(player_y + eye_y * distance_to_wall)

                # Verificar colisiones con el terreno
                if test_x < 0 or test_x >= TERRAIN_WIDTH or test_y < 0 or test_y >= TERRAIN_HEIGHT:
                    hit_wall = True
                    distance_to_wall = TERRAIN_WIDTH
                else:
                    if terrain[test_x // CELL_SIZE][test_y // CELL_SIZE] >= 0.5:
                        hit_wall = True

            # Calcular la altura de la pared en el campo de visión
            wall_height = WINDOW_HEIGHT / (distance_to_wall * math.cos(math.radians(ray_angle - player_angle)))

            # Calcular el color de la pared según la altura
            wall_color = (int(255 / (wall_height / 100)), int(255 / (wall_height / 100)), int(255 / (wall_height / 100)))

            # Dibujar la pared en el campo de visión
            all_color = (int(255 / (wall_height / 100)), int(255 / (wall_height / 100)), int(255 / (wall_height / 100)))
            wall_color_rgb = pygame.Color(*wall_color)
            pygame.draw.rect(window, wall_color_rgb, (ray, (WINDOW_HEIGHT - wall_height) / 2, 1, wall_height))
            # Dibujar el terreno
            draw_terrain(terrain)

        # Dibujar la posición y ángulo del jugador
        pygame.draw.circle(window, (255, 0, 0), (int(player_x), int(player_y)), 5)
        pygame.draw.line(window, (255, 0, 0), (player_x, player_y), (player_x + math.cos(math.radians(player_angle)) * 20, player_y - math.sin(math.radians(player_angle)) * 20))

        pygame.display.update()
        clock.tick(60)

# Ejecutar el juego
if __name__== "__main__":
    main()