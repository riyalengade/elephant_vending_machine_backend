"""Library function to run experiments on the vending machine
"""
import os
import random
from elephant_vending_machine import elephant_vending_machine
from elephant_vending_machine import APP, Screens
from elephant_vending_machine.Screens import Screens

L_screen = Screens() # Left Screen 
M_screen = Screens() # Middle screen 
R_screen = Screens() # Right Screen 
INTER_TRIAL_TIME = 0 # Time interval in between trials 


def display_stimuli(screen_number, stimuli, correct_stimuli):
    """Function to display stimuli to designated screen number. 
	
	Args:
    screen_number (int): The first screen to display stimuli to. Must be an int 1-3.
    stimuli (str): Image file of stimuli. Must have file extension .jpg or .png 
    correct_stimuli (boolean): flag to indicate if this stimuli is the correct one for the current trial
    """
    if(screen_number == 1):
        L_screen.set_stimuli(stimuli)
        L_screen.set_stimuli_flag(correct_stimuli)
    elif(screen_number == 2):
        M_screen.set_stimuli(stimuli)
        M_screen.set_stimuli_flag(correct_stimuli)
    else:
        R_screen.set_stimuli(stimuli)
        R_screen.set_stimuli_flag(correct_stimuli)

def randomize_stimuli(screen1, screen2): 
    """Stimuli will be randomly displayed to the two screens throughout all trials.
    """
    random_num = random.randint(1,2) # if random_num == 1, stimuli on screens stay the same, else, switch stimuli on screen 
    if(random_num == 2):
        temp_screen = Screens(); 
        temp_stimuli=screen1.get_stimuli()
        temp_screen.set_stimuli(temp_stimuli)
        temp_screen.set_screen(screen1.get_screen_num())
        temp_screen.set_stimuli_flag(screen1.get_stimuli_flag())

        screen1.set_stimuli(screen2.get_stimuli())
        screen1.set_screen(screen2.get_screen_num())
        screen1.set_stimuli_flag(screen2.get_stimuli_flag())

        screen2.set_stimuli(temp_screen.get_stimuli())
        screen2.set_screen(temp_screen.get_screen_num())
        screen2.set_stimuli_flag(temp_screen.get_stimuli_flag())

def set_intertrial_time(time):
    """Function to designate the amount of time to wait between trials.
	
	Args:
		time (int): The amount of time to wait between trials in seconds. Must be positive.
    """
    response = ''
    if(time >= 1):
        INTER_TRIAL_TIME = time 
        response = 'set inter-trial time to ' + str(INTER_TRIAL_TIME)
    else: 
        response = 'Invalid time. Must be positive and greater than 0.'
    return response


    

    
    
    





