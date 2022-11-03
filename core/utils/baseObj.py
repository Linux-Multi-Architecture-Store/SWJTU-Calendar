from datetime import datetime
import os
from bs4 import BeautifulSoup as bs

from core.utils import START_AND_END_TIMES
from core.utils.utils import find_date_from_string, create_2D_list, get_class_info_from_str


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
        return self.year + self.date + self.start_time + "00"

    def get_end_time(self):
        return self.year + self.date + self.end_time + "00"


class ClassInfo:
    """
    Base class for SWJTU standard Class instances
    """
    def __init__(self, info: list):
        """
        Accept [ index_number, name, place, start_time, stop_time , day]
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


class ClassTableInfo:
    def __init__(self, html: ClassTableHTML):
        self.raw_data = create_2D_list()
        self.classes: dict[list[type]] = ...

        self._find_raw_class_data(html)

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
                    info = get_class_info_from_str(class_)
                    start_time = START_AND_END_TIMES[j][0]
                    end_time = START_AND_END_TIMES[j][1]
                    day = html.dates[i]
                    day = day[0] + day[1]

                    info[-3] = start_time + "00"
                    info[-2] = end_time + "00"
                    info[-1] = day

                    time = ClassTime(
                        date=html.dates[i],
                        start_time=START_AND_END_TIMES[j][0],
                        end_time=START_AND_END_TIMES[j][1]
                    )

                    this_class = ClassInfo(
                        name=info[1],

                    )

                    # Judge if current class is register in self.classes
                    _is_registered = False
                    for each in self.classes:
                        if each == info[0]:
                            _is_registered = True
                    if not _is_registered:
                        _new_class = {info[0]: []}
                        self.classes.update(_new_class)

                    # Judge if class is added.
                    added = False
                    for each in self.classes[info[0]]:
                        if each[0] == info[0]:
                            if each[-1] == info[-1]:  # if same day, extend.
                                if each[2] == info[2]:  # if is the same classroom, extend.
                                    added = True
                                    if info[-3] < each[-3]:
                                        each[-3] = info[-3]
                                    if info[-2] > each[-2]:
                                        each[-2] = info[-2]

                    if not added:
                        self.classes[info[0]].append(info)
