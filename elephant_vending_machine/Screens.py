"""Screen class object to store info about each screen's number, stimuli to display, and if the screen is the correct stimuli or not
"""
class Screens:

    def __init__(self):
        self.screen_number = ''
        self.stimuli = ''
        self.correct_stimuli = ''

    def set_screen(self, screen_number):
        self.screen_number = screen_number

    def set_stimuli(self,stimuli):
        self.stimuli = '~/images/' + stimuli

    def set_stimuli_flag(self, correct_flag):
        self.correct_stimuli = correct_flag

    def get_screen_num(self):
        return self.screen_number

    def get_stimuli(self):
        return self.stimuli

    def get_stimuli_flag(self):
        return self.correct_stimuli

    