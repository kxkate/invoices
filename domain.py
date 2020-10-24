class Reporter:
    def generate_report(self) -> str:
        pass


class Notifier:
    def notify(self, message: str):
        pass


class Application:  # agreguje R i N
    def __init__(self, reporter: Reporter, notifier: Notifier):
        self._reporter = reporter
        self._notifier = notifier

    def process(self):
        report = self._reporter.generate_report()  # odwoła sie do instancji klasy Reporter i pobiera raport
        self._notifier.notify(f"The following report has been generated:{report}")




