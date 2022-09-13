from bs4 import BeautifulSoup as bs
import re


def _find_date_from_string(str_):
    str_ = str(str_)

    pattern = r"\d.*[日]"
    date_full = re.search(pattern, str_)

    pattern = r"\d*[^月]"
    input_ = date_full[0]
    month = re.search(pattern, input_)
    month = int(month[0])

    pattern = r"[月]\d*[^日]"
    input_ = date_full[0]
    day = re.search(pattern, input_)
    pattern = r"\d.*"
    input_ = day[0]
    day = re.search(pattern, input_)
    day = day[0]
    day = int(day)

    return month, day


class SWJTUCalendar:
    def __init__(self, filepath):
        """
        :param filepath: Path to html calendar file.
        :type filepath: str
        """
        self._file = None
        self._trs = None
        self._titles = []

        self._dates = [i for i in range(7)]
        # [[9, 12], [9, 13], [9, 14], [9, 15], [9, 16], [9, 17], [9, 18]]

        self._read_file(filepath)
        self._get_dates()

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

    class _GetClasses:
        def __init__(self, trs, section):
            self.trs = trs
            # Get required row and columns
            self.tds = self.trs[section].find_all("td")
            self.classes = []
            self._sort_classes()

        def _sort_classes(self):
            """
            Get classes from content.
            :return:
            """
            data = [i for i in range(9)]
            # Judge if there is a class.
            for i, each in enumerate(self.tds):
                text = each.text
                if text != ' ':
                    data[i] = text
                else:
                    data[i] = None
            # TODO: Finish this part.

    def calendar(self):
        return self._file

    def date(self):
        return self._dates