from core.utils import ClassTableHTML, ClassTableInfo


class SWJTUCalendar:
    def __init__(self, filepath, week):
        self.html = ClassTableHTML(filepath, week)
        self.classtable = ClassTableInfo(self.html)

