from unittest.mock import Mock
import pytest

from domain import Reporter, Notifier, Application


#żeby funkcja stała się fixturą, uzywamy dekoratora

@pytest.fixture
def reporter():
    instance = Reporter()
    instance.generate_report = Mock()
    instance.generate_report.return_value = "42"
    return instance  # alt + Enter: import

@pytest.fixture
def notifier():
    instance = Notifier()
    instance.notify = Mock()  #sprawdzamy, czy notify został wywołany raz z wynikiem 42
    return instance

@pytest.fixture
def application(reporter, notifier):
    return Application(reporter,notifier)
    # jak mamy w argumentach reporter i notifier, ktore tez sa fiksturami, to tutaj mamy instancje
    # dependency injection

def test_should_send_prepared_report(application):  # tutaj mamy obiekt klasy Application
    application.process()  # uruchamiamy metodę process

    application._notifier.notify.assert_called_once_with("The following report has been generated:42")
# fikstury - obiekty pomocniecz,e ktore mozna dodac do testu
# asercja przez mockowanie
# zamockujemy to, co zwraca funkcja generate_report
# mozna zamockowac metody, nie tylko klasy itp
# atrybut notifier, metoda notif, metoda assert na mocku
