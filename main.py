try:
    import pygame
except ImportError as e:
    print("There was an import error: " + e)

if __name__ == "__main__":
    # Initialize Screen
    WIDTH, HEIGHT = 1200, 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Rendering")