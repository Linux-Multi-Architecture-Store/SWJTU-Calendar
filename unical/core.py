from .core import ClassTableHTML, ClassTableInfo, ClassInfo
from .core.base import ClassIcs
from .core.saveclasstable import save_given_week_table_html
import tempfile

# Here, HTML files will be stored in system temporary directory.

class SWJTUCalendar:
    def __init__(self, week):
        self.html = None
        self.class_table = ClassTableInfo(self.html, ClassInfo)
        self.ics = ClassIcs(self.class_table)

    def save_to_file(self, path, type="ics") -> str:
        if type == "ics":
            saved_path = self.ics.save_as_ics(path=path)
            return saved_path

        raise Exception("Wrong save type")

    def download_html_file(self, password, username, week):
        temppath = tempfile.mkdtemp()
        _path = save_given_week_table_html(week, username, password, temppath)

        return _path

    def process_html_file(self, filepath, week):
        self.html = ClassTableHTML(filepath, week)

