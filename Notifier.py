

class Notifier:
    """ a class to notify the user of some events """
    def __init__(self, verbose = True):
        self.verbose = verbose

    def notify(self, text, power = 1):
        if(self.verbose)or(power>1):
            print(text)
