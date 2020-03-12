import pytest
from elephant_vending_machine import elephant_vending_machine
from elephant_vending_machine import helper_library, Screens
from elephant_vending_machine.Screens import Screens

@pytest.fixture
def screen1():
    screen_1 = Screens()
    screen_1.set_screen(1)
    screen_1.set_stimuli('/images/test_image.jpeg')
    screen_1.set_stimuli_flag(False)
    return screen_1

@pytest.fixture
def screen2(): 
    screen_2 = Screens()
    screen_2.set_screen(2)
    screen_2.set_stimuli('/images/test_image2.jpeg')
    screen_2.set_stimuli_flag(False)
    return screen_2

@pytest.fixture
def screen3(): 
    screen_3 = Screens()
    screen_3.set_screen(3)
    screen_3.set_stimuli('/images/test_image3.jpeg')
    screen_3.set_stimuli_flag(True)
    return screen_3

def test_display_stimuli_one(screen1):
    helper_library.display_stimuli(1, '/images/test_image.jpeg', False)
    assert helper_library.L_screen.get_stimuli() == '/images/test_image.jpeg'
    assert helper_library.L_screen.get_stimuli_flag() == False

def test_display_stimuli_two(screen2): 
    helper_library.display_stimuli(2, '/images/test_image2.jpeg', False)
    assert helper_library.M_screen.get_stimuli() == '/images/test_image2.jpeg'
    assert helper_library.M_screen.get_stimuli_flag() == False

def test_display_stimuli_three(screen3): 
    helper_library.display_stimuli(3, '/images/test_image3.jpeg', True)
    assert helper_library.R_screen.get_stimuli() == '/images/test_image3.jpeg'
    assert helper_library.R_screen.get_stimuli_flag() == True
  

def test_inter_trial_time():
    time = 0
    assert  helper_library.set_intertrial_time(time)  == 'Invalid time. Must be positive and greater than 0.'

def test_inter_trial_time():
    time = 5
    assert  helper_library.set_intertrial_time(time)  == 'set inter-trial time to 5'