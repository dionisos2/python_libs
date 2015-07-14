"""
See Notifier class
"""

import sys

class Notifier:
    """ a class to notify the user of some events """
    def __init__(self, verbose=True):
        self.verbose = verbose

    def notify(self, text, power=1):
        """ notify the user by different mean """
        if self.verbose or power > 1:
            sys.stdout.buffer.write(text.encode('utf-8'))
            print('')

    def toogle_verbose(self):
        """ Toogle the value of verbose """
        self.verbose = not self.verbose
