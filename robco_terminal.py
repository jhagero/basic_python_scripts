import os
import sys
import time
import random

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def fallout_print(text="", delay=0.01, end='\n', color=bcolors.GREEN, beep=True):
    """
    Print text one character at a time, like a Fallout terminal.
    
    Args:
        text (str): The text to print.
        delay (float): Base delay between characters in seconds.
                       Use a small random variation for more realism.
        end (str): What to print at the end (like print()'s end parameter).
        color: GREEN, YELLOW, ENDC
        beep (bool): Adds terminal bell
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Force immediate display
        if beep and char not in ' \n\t':
            print('\a', end='', flush=True) # Terminal bell
        # Optional: add slight randomness for more "mechanical" feel
        time.sleep(delay + random.uniform(0, 0.02))
    sys.stdout.write(end)
    sys.stdout.flush()




fallout_print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK", delay=0.03)
fallout_print("> INITIALIZING...", delay=0.02)
fallout_print("PASSWORD REQ><sequence interrupted!", delay=0.01)
fallout_print("ERR!:UNAUTH.!!?,<<D!KJ>><>ED#&#//", delay=0.01)
fallout_print(">>ACCESS GRANTED>>", delay=0.03)