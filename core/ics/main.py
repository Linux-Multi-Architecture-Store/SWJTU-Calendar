import os
import re
import json
import time
import uuid


class Ics:
    def __init__(self):
        self.ics = None
        self.data_list = None
        self._load_default()
        self.num_events = 0

    def _load_default(self):
        with open("core/ics/sample.json", mode="r", encoding="utf-8") as f:
            json_ = f.read()
            self.ics = json.loads(json_)

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

    def create_task(self, info) -> None:
        """
        This is the function to create task.
        [name, "2022", "091300", "081200", "0913", place]
        :param info: [name, year, start_time, end_time, date, place]
        :type info: list
        :return:
        """
        time_start = info[1] + info[4] + "T" + info[2]
        time_stop = info[1] + info[4] + "T" + info[3]

        with open("core/ics/task.json", mode="r", encoding="utf-8") as f:
            json_ = f.read()
            task = json.loads(json_)
        task["VEVENT"]['CREATED'] = "19890917T020000"
        task["VEVENT"]['UID'] = str(uuid.uuid4()).upper()
        task["VEVENT"]["DTEND;TZID=Asia/Shanghai"] = time_stop
        task["VEVENT"]["DTSTART;TZID=Asia/Shanghai"] = time_start
        task["VEVENT"]['SUMMARY'] = info[0]
        task["VEVENT"]['LOCATION'] = info[5]
        task["VEVENT"]["SEQUENCE"] = str(self.num_events + 1)

        add = {"task_identify" + str(self.num_events + 1): task}

        self.ics['VCALENDAR'].update(add)
        self.num_events += 1
