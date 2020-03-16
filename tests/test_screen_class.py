import pytest
from elephant_vending_machine import elephant_vending_machine
from elephant_vending_machine import screens
from elephant_vending_machine.screens import Screen

@pytest.fixture
def screen1():
    return Screen()

@pytest.fixture
def screen2():
    return Screen()

def test_set_screen_one(screen1): 
    screen1.set_screen(1)
    assert screen1.screen_number == 1

def test_set_screen_two(screen2): 
    screen2.set_screen(2)
    assert screen2.screen_number == 2

def test_set_stimuli_screen_one(screen1):
    screen1.set_stimuli('/images/test_image.jpeg')
    assert screen1.stimuli == '/images/test_image.jpeg'

def test_set_stimuli_screen_two(screen2):
    screen2.set_stimuli('/images/test_image2.jpeg')
    assert screen2.stimuli == '/images/test_image2.jpeg'

def test_set_stimuliflag_one(screen1):
    screen1.set_stimuli_flag(False)
    assert screen1.correct_stimuli == False

def test_set_stimuliflag_two(screen2):
    screen2.set_stimuli_flag(True)
    assert screen2.correct_stimuli == True

def test_get_screen_num_one(screen1):
    screen1.set_screen(1)
    assert screen1.get_screen_num() == 1

def test_get_screen_num_two(screen2):
    screen2.set_screen(2)
    assert screen2.get_screen_num() == 2

def test_get_stimuli_one(screen1):
    stimuli_test = '/images/test_image.jpeg'
    screen1.set_stimuli('/images/test_image.jpeg')
    assert screen1.get_stimuli()== stimuli_test 

def test_get_stimuli_two(screen2):
    screen2.set_stimuli('/images/test_image2.jpeg')
    assert screen2.get_stimuli() == '/images/test_image2.jpeg' 

def test_get_stimuli_flag_one(screen1):
    screen1.set_stimuli_flag(False)
    assert screen1.get_stimuli_flag() == False 

def test_get_stimuli_flag_two(screen2):
    screen2.set_stimuli_flag(True)
    assert screen2.get_stimuli_flag() == True