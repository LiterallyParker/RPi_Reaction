import time
import pygame

def init_controller():
    # Initialize pygame's joystick module
    pygame.init()
    pygame.joystick.init()

    # Check if a joystick is connected
    controller_count = 0
    while controller_count == 0:
        print("Searching for controller...")
        pygame.joystick.init()
        controller_count = pygame.joystick.get_count()
        time.sleep(0.2)

    # Initialize the first joystick
    controller = pygame.joystick.Joystick(0)
    controller.init()
    return controller