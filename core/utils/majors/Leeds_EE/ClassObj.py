from core.utils import ClassInfo

class LeedsClassInfo(ClassInfo):
    def __init__(self, name=None, date=None, place=None, time=None):
        super(LeedsClassInfo, self).__init__(name=name, date=date, place=place, time=time)

        """
        This is the class type.
        In the Joint School, classes are devided into following parts:
        1. Lectures, L
        2. Laboratory, Lab
        3. Examination/Exercises, E
        4. Tutorials, T
        """
        self.class_type = None