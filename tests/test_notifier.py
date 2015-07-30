import sys

sys.path.append('./')
from notifier import Notifier

def test_constants():
    assert Notifier.NO_OUTPUT == ('verbosity', -2)
    assert Notifier.QUIET == ('verbosity', -1)
    assert Notifier.NORMAL == ('verbosity', 0)
    assert Notifier.VERBOSE == ('verbosity', 1)
    assert Notifier.DEBUG == ('verbosity', 2)

    assert Notifier.DEBUG_INFO == ('power', -2)
    assert Notifier.BASIC == ('power', -1)
    assert Notifier.WARNING == ('power', 0)
    assert Notifier.ERROR == ('power', 1)

def test_should_notify():
    NO_OUTPUT = Notifier.NO_OUTPUT
    QUIET = Notifier.QUIET
    NORMAL = Notifier.NORMAL
    VERBOSE = Notifier.VERBOSE
    DEBUG = Notifier.DEBUG

    DEBUG_INFO = Notifier.DEBUG_INFO
    BASIC = Notifier.BASIC
    WARNING = Notifier.WARNING
    ERROR = Notifier.ERROR
    should_notify = Notifier.should_notify

    assert not should_notify(NO_OUTPUT, ERROR)
    assert not should_notify(NO_OUTPUT, DEBUG_INFO)

    assert should_notify(QUIET, ERROR)
    assert not should_notify(QUIET, WARNING)

    assert should_notify(NORMAL, WARNING)
    assert not should_notify(NORMAL, BASIC)

    assert should_notify(VERBOSE, BASIC)
    assert not should_notify(VERBOSE, DEBUG_INFO)

    assert should_notify(DEBUG, DEBUG_INFO)
    assert should_notify(DEBUG, ERROR)
