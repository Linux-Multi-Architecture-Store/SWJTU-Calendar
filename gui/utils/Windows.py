import dearpygui.dearpygui as dpg
from src.infos import APP_VERSION

def new_alert(title, message1, message2):
    with dpg.window(label=str(title)) as window:
        dpg.add_text(default_value=message1 if message1 is not None else message2)


def about_programme():
    with dpg.window(label="关于") as window:
        dpg.add_text(
            default_value="SWJTU 课表小工具"
        )
        dpg.add_text(
            default_value=APP_VERSION
        )
        dpg.add_text(
            default_value="Copyright © 2022-Now Yinan Qin"
        )
        dpg.add_text(
            default_value="This software is licensed \n under the MIT license."
        )
    return window
