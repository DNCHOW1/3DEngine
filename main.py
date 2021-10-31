try:
    import pygame
    import sys
except ImportError as e:
    print("There was an import error: " + e)
    sys.exit(2)

def main():
    # Initialize Screen
    WIDTH, HEIGHT = 600, 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Rendering")

    # Initialize Black Background
    background = pygame.Surface(screen.get_size())
    background = background.convert() # The standard to improve performance
    background.fill((0, 0, 0))

    # "Drawing" to the screen
    screen.blit(background, (0, 0))

    # Updating the screen (imagine it like a whiteboard you can flip)
    pygame.display.flip()

    # Event loop
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30) # Runs at 30 frames
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(background, (0, 0)) # Erasing previous contents on the board
        # ...
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        sys.exit()