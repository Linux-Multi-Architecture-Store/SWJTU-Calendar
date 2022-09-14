from bs4 import BeautifulSoup as bs
import re
import numpy as np
from datetime import datetime

import core.ics as ics


def _find_date_from_string(str_):
    str_ = str(str_)

    pattern = r"\d.*[日]"
    date_full = re.search(pattern, str_)

    pattern = r"\d*[^月]"
    input_ = date_full[0]
    month = re.search(pattern, input_)
    month = str(month[0])

    pattern = r"[月]\d*[^日]"
    input_ = date_full[0]
    day = re.search(pattern, input_)
    pattern = r"\d.*"
    input_ = day[0]
    day = re.search(pattern, input_)
    day = day[0]
    day = str(day)

    return month, day


def _get_class_info_from_str(string):
    # [ index_number, name, place, start_time, stop_time , day]

    infos = string.split()

    """
    Some classes have a letter after the index, such as:
    B4417  T  通信系统概论（肖嵩）2-5,15周 X30548
    Thus we need to judge the second item is letters or not.
    """
    index_number = infos[0]
    place = infos[-1]
    if not infos[1].isalpha():  # If it is not an alpha
        name = infos[1]
    else:
        name = infos[2]

    pattern = "[\u4e00-\u9fa5]*[^（]"
    name_found = re.search(pattern, name)
    name_found = name_found[0]
    name = str(name_found)

    full = [index_number, name, place, "", "", ""]

    return full


class SWJTUCalendar:
    def __init__(self, filepath):
        """
        :param filepath: Path to html calendar file.
        :type filepath: str
        """
        self._file = None
        self._trs = None
        self._titles = []

        self.start_end_times = [
            ["0800", "0845"],
            ["0850", "0935"],
            ["0950", "1035"],
            ["1040", "1125"],
            ["1130", "1215"],
            ["1400", "1445"],
            ["1450", "1535"],
            ["1550", "1635"],
            ["1640", "1725"],
            ["1730", "1815"],
            ["1930", "2015"],
            ["2020", "2105"],
            ["2110", "2155"]
        ]
        self._dates = [[9, 12], [9, 13], [9, 14], [9, 15], [9, 16], [9, 17], [9, 18]]

        self._classes = np.random.randn(7, 13).astype('<U2000')
        self._classes_found = []
        """
        Elements in self._classes_found should be:
        [ index_number, name, place, start_time, stop_time , day]
        All the item should be str.
        """

        self.ics = ics.Ics()

        self._read_file(filepath)
        self._get_dates()
        self._sort_classes()
        self._read_and_integrate_class_info()
        self._add_class_to_calendar()
        print()

    def _read_file(self, file):
        with open(file, mode="r", encoding="utf-8-sig") as f:
            data = bs(f, features="html5lib")
            table = data.find("table", class_="table_border")
            self._file = table.find("tbody")
            self._trs = self._file.find_all("tr")

    def _get_dates(self):
        title_tr = self._trs[0]
        tds = title_tr.find_all("td")

        for each in tds:
            title = each.text
            self._titles.append(title)

        for i in range(-1, -8, -1):
            title = str(self._titles[i])
            month, day = _find_date_from_string(self._titles[i])
            self._dates[i] = [month, day]

    def _sort_classes(self):
        """
        Get classes from content.
        :return:
        """
        for section in range(1, 14, 1):
            tds = self._trs[section].find_all("td")
            data = [i for i in range(9)]
            # Judge if there is a class.
            for i, each in enumerate(tds):
                text = each.text
                if text != ' ':
                    data[i] = text
                else:
                    data[i] = None
            # store in self._classes
            for i, each in enumerate(data):
                if i <= 1:
                    pass
                self._classes[i - 2][section - 1] = each

    def _read_and_integrate_class_info(self):

        for i, each in enumerate(self._classes):
            for j, class_ in enumerate(each):
                if class_ != "None":
                    info = _get_class_info_from_str(class_)
                    start_time = self.start_end_times[j][0]
                    end_time = self.start_end_times[j][1]
                    day = self._dates[i]
                    day = day[0] + day[1]

                    info[-3] = start_time + "00"
                    info[-2] = end_time + "00"
                    info[-1] = day

                    # Judge if class is added.
                    added = False
                    for each in self._classes_found:
                        if each[0] == info[0]:
                            if each[-1] == info[-1]:  # if same day, extend.
                                added = True
                                if info[-3] < each[-3]:
                                    each[-3] = info[-3]
                                if info[-2] > each[-2]:
                                    each[-2] = info[-2]

                    if not added:
                        self._classes_found.append(info)

    def _add_class_to_calendar(self):
        year = str(datetime.now().year)
        for each in self._classes_found:
            self.ics.create_task([
                each[1], year, each[-3], each[-2], each[-1], each[2]
            ])

    def save_calendar(self) -> None:
        self.ics.generate_data_dict()
        self.ics.save_file()


