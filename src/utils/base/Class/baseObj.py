from datetime import datetime
import os
from bs4 import BeautifulSoup as bs

from src.utils.constants import START_AND_END_TIMES
from src.utils.utils import find_date_from_string, create_2D_list, get_class_info_from_str

import re


class ClassTime:
    """
    Store the date & time info for a class
    """

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
        return self.year + self.date + "T" + self.start_time + "00"

    def get_end_time(self):
        return self.year + self.date + "T" + self.end_time + "00"

    def __eq__(self, other):
        if self.year == other.year:
            if self.date == other.date:
                if self.start_time == other.start_time:
                    if self.end_time == other.end_time:
                        return True

        return False

    def __lt__(self, other):
        if self.year == other.year:
            if self.date == other.date:
                if self.start_time < other.start_time:
                    if self.end_time < other.end_time:
                        return True
        return False

    def __gt__(self, other):
        if self.year == other.year:
            if self.date == other.date:
                if self.start_time > other.start_time:
                    if self.end_time > other.end_time:
                        return True
        return False


class ClassInfo:
    """
    Base class for SWJTU standard Class instances
    """

    def __init__(self, class_string: str, ctime: ClassTime) -> None:
        """
        Accept standard class instances, e.g.

        B1349  马克思主义基本原理（郑瑶） 1-17周 X1328
        """
        self.name = ...
        self.place = ...
        self.time = ctime
        self.index_number = ...
        self.teacher_name = ...

        self.infos = class_string.split()

        self.place = self.infos[-1]
        self.get_class_name()
        self.get_class_index_number()
        self.get_teacher_name()

    def get_class_name(self) -> None:
        pattern = "[\u4e00-\u9fa5]*[^（]"
        name_found = re.search(pattern, self.infos[1])
        name_found = name_found[0]
        name = str(name_found)

        self.name = name

    def get_class_index_number(self) -> None:
        self.index_number = self.infos[0]

    def get_teacher_name(self) -> None:
        pattern = r"[\uff08][\u4e00-\u9fa5]*[\uff09]"
        name_found = re.search(pattern, self.infos[1])
        name_found = name_found[0]
        name = str(name_found).strip("\uff08\uff09")

        self.teacher_name = name

    def __eq__(self, other):
        if self.index_number == other.index_number:
            if self.place == other.place:
                if self.time == other.time:
                    return True
        return False

    def __lt__(self, other):
        if self.index_number == other.index_number:
            if self.place == other.place:
                if self.time < other.time:
                    return True
        return False

    def __gt__(self, other):
        if self.index_number == other.index_number:
            if self.place == other.place:
                if self.time > other.time:
                    return True
        return False


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


class ClassTableInfo:
    def __init__(self, html: ClassTableHTML, ClassType: type):
        self.raw_data = create_2D_list()
        self.classes: dict[list[type]] = ...

        self._find_raw_class_data(html)
        self._read_and_integrate_class_info(html, ClassType)

    def _find_raw_class_data(self, html: ClassTableHTML):
        for section in range(1, 14, 1):
            tds = html.trs[section].find_all("td")
            data = [i for i in range(9)]
            # Judge if there is a class.
            for i, each in enumerate(tds):
                text = each.text
                if not text.isspace():
                    data[i] = text
                else:
                    data[i] = None
            # store in self._raw_classes
            for i, each in enumerate(data):
                if i <= 1:
                    pass
                self.raw_data[i - 2][section - 1] = each

    def _read_and_integrate_class_info(self, html: ClassTableHTML, ClassType: type):

        for i, each in enumerate(self.raw_data):
            for j, class_ in enumerate(each):
                if class_ is not None:
                    time = ClassTime(
                        date=html.dates[i],
                        start_time=START_AND_END_TIMES[j][0],
                        end_time=START_AND_END_TIMES[j][1]
                    )

                    this_class = ClassType(
                        class_string=class_,
                        ctime=time
                    )

                    # Judge if current class is register in self.classes
                    _is_registered = False
                    for each in self.classes:
                        if each == this_class.index_number:
                            _is_registered = True
                    if not _is_registered:
                        _new_class = {this_class.index_number: []}
                        self.classes.update(_new_class)

                    # Judge if class is added.
                    added = False

                    for each in self.classes[this_class.index_number]:
                        if each == this_class:
                            added = True
                            break
                        if each > this_class:
                            each.time.start_time = this_class.time.start_time
                            added = True
                            break
                        if each < this_class:
                            each.time.end_time = this_class.time.end_time
                            added = True
                            break

                    if not added:
                        self.classes[this_class.index_number].append(this_class)
