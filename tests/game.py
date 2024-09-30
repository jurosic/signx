# Imports
import sys
import pygame

# Pygame Configuration
pygame.init()
fps = 300
fpsClock = pygame.time.Clock()
width, height = 800, 800
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)


# Initial color
drawColor = [0, 0, 0]

# Initial brush size
brushSize = 3
brushSizeSteps = 1

# Drawing Area Size
canvasSize = [800, 800]


# Canvas
canvas = pygame.Surface(canvasSize)
canvas.fill((255, 255, 255))

# Game loop.
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the Canvas at the center of the screen
    x, y = screen.get_size()
    screen.blit(canvas, [x/2 - canvasSize[0]/2, y/2 - canvasSize[1]/2])

    # Drawing with the mouse
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()

        # Calculate Position on the Canvas
        dx = mx - x/2 + canvasSize[0]/2
        dy = my - y/2 + canvasSize[1]/2

        pygame.draw.circle(
            canvas,
            drawColor,
            [dx, dy],
            brushSize,
        )

    # Reference Dot
    pygame.draw.circle(
        screen,
        drawColor,
        [100, 100],
        brushSize,
    )

    pygame.display.flip()
    fpsClock.tick(fps)
