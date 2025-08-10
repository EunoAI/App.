import pygame


def create_window(size=(800, 600)):
    """Create a display window.

    Tries to create a fullscreen window first and falls back to windowed mode if
    fullscreen fails (for example, when running in environments that do not
    support a fullscreen display).
    """
    try:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    except pygame.error:
        screen = pygame.display.set_mode(size)
    return screen


if __name__ == "__main__":
    pygame.init()
    screen = create_window()
    pygame.display.set_caption("Game Window")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()
