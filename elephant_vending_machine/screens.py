"""Screen class object to store info about each screen object
"""
class Screen:
    """Screen class object has each screen's number, stimuli to display,
    and if the screen is the correct stimuli or not
    """

    def __init__(self):
        self.screen_number = 0
        self.stimuli = ''
        self.correct_stimuli = ''

    def set_screen(self, screen_number):
        """Function to set screen's number

        Parameters:
        self: instance of screen class
        screen_number (int): specifies which screen out of the three on
        the vending machine. Must be an int 1-3.
        """
        if screen_number >= 1 & screen_number <= 3:
            self.screen_number = screen_number

    def set_stimuli(self, stimuli):
        """Function to set screen's stimuli image
        Parameters:
        self: instance of screen class
        screen_number (str): path to the image stimuli
        """
        self.stimuli = stimuli

    def set_stimuli_flag(self, correct_flag):
        """Function to set screen's stimuli flag
        Parameters:
        self: instance of screen class
        correct_flag(boolean): true or false
        """
        self.correct_stimuli = correct_flag

    def get_screen_num(self):
        """Function to return screen's number"""
        return self.screen_number

    def get_stimuli(self):
        """Function to return screen's stimuli """
        return self.stimuli

    def get_stimuli_flag(self):
        """Function to return screen's stimuli flag"""
        return self.correct_stimuli
