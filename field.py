import pygame

# Const size
SIZE = [500, 600]
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1
# Colors
FRAME_COLORS = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(FRAME_COLORS)

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if column % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK))

    pygame.display.flip()
