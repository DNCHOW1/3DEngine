try:
    import pygame
    import sys
except ImportError as e:
    print("There was an import error: " + e)
    sys.exit(2)

def converted_screen_points(points, scale, cube_pos):
    new_points = [0]*(len(points))
    dx, dy = cube_pos
    for i, (pointx, pointy) in enumerate(points):
        new_points[i] = (pointx*scale + dx, pointy*scale + dy)
    return new_points

def connect_points(surface, points):
    n = len(points)
    for i in range(n):
        pygame.draw.line(surface, (255, 255, 255), points[i], points[(i+1)%n])
    for i in range(n):
        pygame.draw.circle(surface, (255, 0, 0), points[i], 3)

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

    cube_position = [WIDTH//2, HEIGHT//2]
    scale = 100
    points = [
        [-1, -1], # TL
        [1, -1],  # TR
        [1, 1],   # BR
        [-1, 1],  # BL
    ]
    converted = converted_screen_points(points, scale, cube_position)
    connect_points(screen, converted)

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
        # Instead of points, have it be the the result of points and linear transformations
        converted = converted_screen_points(points, scale, cube_position)
        connect_points(screen, converted)
        # ...
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        sys.exit()