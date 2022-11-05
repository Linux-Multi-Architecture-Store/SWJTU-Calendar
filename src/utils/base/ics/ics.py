import os
import re
import json
import time
import uuid
import src.utils.base.ics.randomcolor as randomcolor
from .defaults import DEFAULT_EVENT, DEFAULT_CAL
from ... import ClassTableInfo


class Ics:
    def __init__(self):
        self.ics = None
        self.data_list = None
        self._load_default()
        self.num_events = 0

    def _load_default(self):
        self.ics = json.loads(DEFAULT_CAL)
        self.ics['VCALENDAR']['X-APPLE-CALENDAR-COLOR'] = randomcolor.get_random_colour()

    def change_name(self, name):
        self.ics['VCALENDAR']['X-WR-CALNAME'] = name

    def generate_data_dict(self):
        data_list = []

        def load_dict(input_):
            for each in input_:
                VTASK = re.search(r"task_identify\d*", str(each))
                if VTASK:
                    founded = True
                else:
                    founded = False

                if founded:
                    load_dict(input_[each])
                    continue

                if type(input_[each]) == dict:
                    data_list.append("BEGIN:" + each + "\n")
                    load_dict(input_[each])
                    data_list.append("END:" + each + "\n")
                else:
                    data_list.append(each + ":" + input_[each] + "\n")

        load_dict(self.ics)
        self.data_list = data_list

    def save_file(self, name=None, path=None):
        if path is None:
            path = os.path.curdir
        if name is None:
            name = time.asctime(time.localtime())

        file_full_path = os.path.join(path, name + ".ics")

        with open(file_full_path, mode="w", encoding="utf-8") as f:
            f.writelines(self.data_list)

    def create_task(self, cls_info: type) -> None:
        """
        This is the function to create task.
        [name, "2022", "091300", "081200", "0913", place]
        :param info: [name, year, start_time, end_time, date, place]
        :type info: list
        :return:
        """
        time_start = cls_info.time.get_start_time()
        time_stop = cls_info.time.get_end_time()

        task = json.loads(DEFAULT_EVENT)
        task["VEVENT"]['CREATED'] = "19890917T020000"
        task["VEVENT"]['UID'] = str(uuid.uuid4()).upper()
        task["VEVENT"]["DTEND;TZID=Asia/Shanghai"] = time_stop
        task["VEVENT"]["DTSTART;TZID=Asia/Shanghai"] = time_start
        task["VEVENT"]['SUMMARY'] = cls_info.name
        task["VEVENT"]['LOCATION'] = cls_info.place
        task["VEVENT"]["SEQUENCE"] = str(self.num_events + 1)

        add = {"task_identify" + str(self.num_events + 1): task}

        self.ics['VCALENDAR'].update(add)
        self.num_events += 1

class ClassIcs:
    def __init__(self, cls_table: ClassTableInfo):
        self.ics = {}