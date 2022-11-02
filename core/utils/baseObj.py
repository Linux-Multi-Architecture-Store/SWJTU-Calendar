from datetime import datetime
import os
from bs4 import BeautifulSoup as bs

from core.utils.utils import find_date_from_string


class ClassTime:
    def __init__(self, date, start_time, end_time):
        """

        :param date: [month, day]
        :param start_time: str, "hhmm"
        :param end_time: str, "hhmm"
        """
        self.year = str(datetime.now().year)
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def get_start_time(self):
        return self.year + self.date + self.start_time + "00"

    def get_end_time(self):
        return self.year + self.date + self.end_time + "00"


class Class:
    def __init__(self, name=None, date=None, place=None, time=None,
                 index_number=None):
        """
        Base classe for SWJTU Class instances
        :param name: Name of the class
        :type name: str
        :param date: Date of the class
        :type date: str
        :param place: Place of the class
        :type place: str
        :param time: Time obj of the class
        :type time: ClassTime
        :param index_number: Index number of the class
        :type index_number: str
        """
        self.name = name
        self.date = date
        self.place = place
        self.time = time
        self.index_number = index_number


class ClassTableHTML:
    def __init__(self, filepath, week):
        self.table_body = None
        self.trs = None
        self.dates: list = ...

        self._read_file(filepath, week)
        self._get_dates()

    def _read_file(self, file, index) -> None:
        file = os.path.join(file, str(index) + ".html")

        with open(file, mode="r", encoding="utf-8-sig") as f:
            data = bs(f, features="html5lib")
            table = data.find("table", class_="table_border")
            self.table_body = table.find("tbody")
            self.trs = self.table_body.find_all("tr")

    def _get_dates(self):
        _titles: list = ...
        title_tr = self.trs[0]
        tds = title_tr.find_all("td")

        for each in tds:
            title = each.text
            _titles.append(title)

        for i in range(-1, -8, -1):
            """
            从最后一个往前处理是因为前两个并不是日期...
            """
            title = str(_titles[i])
            month, day = find_date_from_string(_titles[i])
            self.dates.insert(0, [month, day])
