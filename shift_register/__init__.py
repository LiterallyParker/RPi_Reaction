import time
from .init_shift_register import init_shift_register
from .shift_out import shift_out
from .blue_off import blue_off
from .blue_on import blue_on
from .sound_buzzer import sound_buzzer
from .cleanup import cleanup

__all__ = ["init_shift_register", "shift_out", "blue_off", "blue_on", "sound_buzzer", "cleanup"]

if __name__ == "__main__":
    from os import system
    system("clear")
    try:
        init_shift_register()
        patterns = [0b11110000, 0b00001111]
        while True:
            for pattern in patterns:
                shift_out(pattern)
                blue_on()
                sound_buzzer()
                blue_off()
                time.sleep(0.1)  # Adjust speed as needed
            for pattern in reversed(patterns):
                shift_out(pattern)
                blue_on()
                sound_buzzer()
                blue_off()
                time.sleep(0.1)  # Adjust speed as needed
    except KeyboardInterrupt:
        print("\nExiting...")
        cleanup()