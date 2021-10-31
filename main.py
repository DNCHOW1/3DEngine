try:
    import pygame
    import sys
except ImportError as e:
    print("There was an import error: " + e)

def main():
    # Initialize Screen
    WIDTH, HEIGHT = 1200, 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Rendering")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        sys.exit()