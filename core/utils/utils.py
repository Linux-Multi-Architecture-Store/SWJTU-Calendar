import re


def create_2D_list():
    tis = []
    for i in range(7):
        tis.append([])
        for j in range(13):
            tis[i].append("")
    return tis


def find_date_from_string(str_):
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


def get_class_info_from_str(string):
    # [ index_number, name, place, start_time, stop_time , day]
    #ToDo： 识别 Lab,GX 这种格式
    #ToDo： 冲突选课解决！
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
