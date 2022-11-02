from core.utils import ClassTableHTML


class SWJTUCalendar:
    def __init__(self, filepath, week):
        self.html = ClassTableHTML(filepath, week)
