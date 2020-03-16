import pytest
from elephant_vending_machine import elephant_vending_machine
from elephant_vending_machine import helper_library, screens
from elephant_vending_machine.screens import Screen

def test_display_stimuli_one():
    helper_library.display_stimuli(1, '/images/test_image.jpeg', False)
    assert helper_library.L_SCREEN.get_stimuli() == '/images/test_image.jpeg'
    assert helper_library.L_SCREEN.get_stimuli_flag() == False

def test_display_stimuli_two(): 
    helper_library.display_stimuli(2, '/images/test_image2.jpeg', False)
    assert helper_library.M_SCREEN.get_stimuli() == '/images/test_image2.jpeg'
    assert helper_library.M_SCREEN.get_stimuli_flag() == False

def test_display_stimuli_three(): 
    helper_library.display_stimuli(3, '/images/test_image3.jpeg', True)
    assert helper_library.R_SCREEN.get_stimuli() == '/images/test_image3.jpeg'
    assert helper_library.R_SCREEN.get_stimuli_flag() == True
  

def test_inter_trial_time():
    time = 0
    assert  helper_library.set_intertrial_time(time)  == 'Invalid time. Must be positive and greater than 0.'

def test_inter_trial_time():
    time = 5
    assert  helper_library.set_intertrial_time(time)  == 'set inter-trial time to 5'