import pytest

from elephant_vending_machine import elephant_vending_machine
from elephant_vending_machine import helper_library
from elephant_vending_machine.helper_library import helper_library

def test_inter_trial_time():
    time = 0
    assert  helper_library.set_intertrial_time(time)  == 'Invalid time. Must be positive and greater than 0.'

def test_inter_trial_time():
    time = 5
    assert  helper_library.set_intertrial_time(time)  == 'set inter-trial time to 5'