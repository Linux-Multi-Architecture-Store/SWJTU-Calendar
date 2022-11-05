from src.utils import ClassTableHTML, ClassTableInfo, ClassInfo


class SWJTUCalendar:
    def __init__(self, filepath, week):
        self.html = ClassTableHTML(filepath, week)
        self.class_table = ClassTableInfo(self.html, ClassInfo)


    def _create_icses_from_classes(self):
        for each in self.classes:
            _ics = ics.Ics()
            _ics.change_name(self.classes_name[each])
            _new_dict = {each: _ics}
            self.ics.update(_new_dict)

        for each in self.classes:
            self._add_class_to_calendar(each, self.classes[each])