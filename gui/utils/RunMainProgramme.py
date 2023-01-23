import dearpygui.dearpygui as dpg
import threading

from gui.utils.Windows import new_alert
from src.utils import save_given_week_table_html, ClassTableInfo, ClassTableHTML, ClassInfo
from src.utils.base import ClassIcs


def MainProcess():

    html_path = save_given_week_table_html(
        week_num=int(dpg.get_value("selected_week")),
        username=dpg.get_value("username"),
        password=dpg.get_value("password"),
        path=dpg.get_value("selected_saving_path")
    )
    class_html = ClassTableHTML(html_path, int(dpg.get_value("selected_week")))
    calendar = ClassTableInfo(class_html, ClassInfo)
    class_ics = ClassIcs(calendar)

    path_saved = class_ics.save_as_ics(dpg.get_value("selected_saving_path"))
    new_alert("提示", f"任务完成啦，保存在：\n {path_saved}", "")

def StartProcess():
    thread = threading.Thread(target=MainProcess, name="MainProcess")
    thread.daemon = True
    thread.start()
    new_alert("提示", "任务开始啦", "")