import unical.main.utils.web as webtools
import os
import asyncio


def save_all_table_html(username, password, path):
    cookies = webtools.get_cookie(username, password)
    cookies = asyncio.run(cookies)
    temp_path = None
    for i in range(1, 26, 1):  # Total 25 weeks.
        tabel = webtools.get_class_table(cookies, i)
        filename = str(i) + ".html"
        temp_path = os.path.join(path, "temp")
        os.makedirs(temp_path, exist_ok=True)
        filename = os.path.join(temp_path, filename)
        with open(filename, mode="w", encoding="utf-8") as f:
            f.writelines(tabel)
        print("[ info ] Saved table: ", i)
    return temp_path


def save_given_week_table_html(week_num, username, password, path):
    cookies = webtools.get_cookie(username, password)
    cookies = asyncio.run(cookies)
    temp_path = None

    tabel = webtools.get_class_table(cookies, week_num)
    filename = str(week_num) + ".html"
    temp_path = os.path.join(path, "temp")
    os.makedirs(temp_path, exist_ok=True)
    filename = os.path.join(temp_path, filename)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(tabel)
    print("[ info ] Saved table: ", week_num)
    return temp_path
