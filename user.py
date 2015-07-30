"""
Some simple functions to deal with the user
"""

from .notifier import Notifier

def ask_user(choices, notifier=None):
    """ Ask user to choose between the list of choices 'choices', until e does """
    if notifier != None:
        assert isinstance(notifier, Notifier)
        notify = notifier.notify
    else:
        notify = print

    while True:
        notify('Possible choices :' + str(choices))
        choice = input()
        if choice in choices:
            return choice
        else:
            notify('Bad choice, plz retry')
