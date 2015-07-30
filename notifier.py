"""
See Notifier class
"""

import sys

class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()

class Notifier:
    """ a class to notify the user of some events """
    def __init__(self, verbosity=False):
        if verbosity == False:
            verbosity = Notifier.NORMAL

        if verbosity == True:
            verbosity = Notifier.VERBOSE

        assert Notifier.good_verbosity(verbosity)
        self._verbosity = verbosity

    @property
    def verbosity(self):
        """ Level of verbosity """
        return self._verbosity

    def notify(self, text, power=None):
        """ notify the user by different mean """
        if power == None:
            power = Notifier.WARNING

        assert Notifier.good_power(power)

        if Notifier.should_notify(self.verbosity, power):
            sys.stdout.buffer.write(text.encode('utf-8'))
            print('')

    @classmethod
    def good_power(cls, power):
        return power[0] == 'power' and power[1] in range(-2, 2)

    @classmethod
    def good_verbosity(cls, verbosity):
        return verbosity[0] == 'verbosity' and verbosity[1] in range(-2, 3)

    @classmethod
    def should_notify(cls, verbosity, power):
        assert Notifier.good_verbosity(verbosity)
        assert Notifier.good_power(power)
        return power[1] >= -verbosity[1]

    @ClassProperty
    @classmethod
    def DEBUG_INFO(cls):
        """ Very unimportant notification (context informations, etc) """
        return ('power', -2)

    @ClassProperty
    @classmethod
    def BASIC(cls):
        """ Notifications for basic events"""
        return ('power', -1)

    @ClassProperty
    @classmethod
    def WARNING(cls):
        """ Notifications for Warnings or others important events """
        return ('power', 0)

    @ClassProperty
    @classmethod
    def ERROR(cls):
        """ Notifications for Errors """
        return ('power', 1)

    @ClassProperty
    @classmethod
    def NO_OUTPUT(cls):
        """ Never notify. """
        return ('verbosity', -2)

    @ClassProperty
    @classmethod
    def QUIET(cls):
        """ Notify only for Error """
        return ('verbosity', -1)

    @ClassProperty
    @classmethod
    def NORMAL(cls):
        """ Notify for warning and other important things """
        return ('verbosity', 0)

    @ClassProperty
    @classmethod
    def VERBOSE(cls):
        """ Notify for about every steps """
        return ('verbosity', 1)

    @ClassProperty
    @classmethod
    def DEBUG(cls):
        """ Notify for everything(all steps, context informations, etc) """
        return ('verbosity', 2)
