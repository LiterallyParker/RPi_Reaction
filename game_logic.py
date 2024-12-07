import pygame
from shift_register import init_shift_register, shift_out, blue_on, blue_off, sound_buzzer, cleanup
from controller import init_controller

import time

LEVEL = 1  # Start at level 1
SPEED = 0.3  # Initial speed of the light
SCORE = 0
HIGH_SCORE = 0

STATES = [
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00000000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001,
]
CONTROLLER = init_controller()

# Function to increase level and speed
def next_level():
    global LEVEL, SPEED
    if LEVEL < 20:
        LEVEL += 1
        SPEED *= 0.7   # Increase speed
    
def restart():
    global LEVEL, SPEED
    LEVEL = 1
    SPEED = 0.3
    time.sleep(0.3)
        
# Function to run the game loop
def run_game():
    global LEVEL, SPEED, SCORE, HIGH_SCORE
    direction = 1
    current_index = 0
    
    while True:
        for i in range(len(STATES)):
            if direction == 1:
                current_index = i
            else:
                current_index = len(STATES) - 1 - i
                
            blue_off()
            shift_out(STATES[current_index])  # For debugging or printing the state

            if current_index == 4:  # Blue LED state
                blue_on()
                start_time = time.time()
                while time.time() - start_time < SPEED:
                    pygame.event.pump()
                    if CONTROLLER.get_button(0):
                        sound_buzzer()  # Play the buzzer sound
                        next_level()  # Progress to the next level
                        SCORE += 1
                        HIGH_SCORE = max(SCORE, HIGH_SCORE)
                        print("SCORE:", SCORE)
                        print("HIGH SCORE:", HIGH_SCORE)
                        break
            else:
                start_time = time.time()
                while time.time() - start_time < SPEED:
                    pygame.event.pump()
                    if CONTROLLER.get_button(0):
                        restart()
                        SCORE = 0
                        break
            
            time.sleep(SPEED)
            
        direction *= -1
        
# Dummy function to check if the button is pressed (replace with actual logic)

if __name__ == "__main__":
    try:
        init_shift_register()
        
        while True:
            run_game()
    except KeyboardInterrupt:
        cleanup()
        print("Exiting the game!")