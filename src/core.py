from .utils import ClassTableHTML, ClassTableInfo, ClassInfo
from .utils.base import ClassIcs

class SWJTUCalendar:
    def __init__(self, filepath, week):
        self.html = ClassTableHTML(filepath, week)
        self.class_table = ClassTableInfo(self.html, ClassInfo)
        self.ics = ClassIcs(self.class_table)

    def save_to_file(self, path, type="ics") -> str:
        if type == "ics":
            saved_path = self.ics.save_as_ics(path=path)
            return saved_path

        raise Exception("Wrong save type")
