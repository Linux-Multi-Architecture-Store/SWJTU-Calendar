import utils.web as webtools
import os


def save_all_table_html():
    cookies = webtools.get_cookie()
    temp_path = None
    for i in range(1, 26, 1):  # Total 25 weeks.
        tabel = webtools.get_class_table(cookies, i)
        filename = str(i) + ".html"
        temp_path = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_path, exist_ok=True)
        filename = os.path.join(temp_path, filename)
        with open(filename, mode="w", encoding="utf-8") as f:
            f.writelines(tabel)
        print("[ info ] Saved table: ", i)
    return temp_path
