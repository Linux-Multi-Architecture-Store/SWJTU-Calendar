import dearpygui.dearpygui as dpg
import gui.utils as utils
import src.infos
from gui.utils import StartProcess
from src.infos import SUPPORTED_SCHOOL


def App():
    dpg.create_context()

    font = utils.add_fonts_and_dpi("assets/fonts/Source_Code_Pro_and_YaHei.ttf", 1.5)

    with dpg.value_registry():
        dpg.add_string_value(tag="username")
        dpg.add_string_value(tag="password")
        dpg.add_string_value(tag="selected_school")
        dpg.add_string_value(tag="selected_major")
        dpg.add_int_value(tag="selected_week")
        dpg.add_string_value(tag="selected_saving_path")

    with dpg.window(label="Calendar 日历") as main:
        utils.add_menu()

        with dpg.collapsing_header(label="统一身份认证"):
            with dpg.group(horizontal=True):
                dpg.add_text("用户名：")
                dpg.add_input_text(source="username")
            with dpg.group(horizontal=True):
                dpg.add_text("密  码：")
                dpg.add_input_text(source="password", password=True)

        with dpg.collapsing_header(label="导出设置"):
            with dpg.group(horizontal=True):
                dpg.add_text("学院模板：")
                dpg.add_combo(
                    items=SUPPORTED_SCHOOL,
                    source="selected_school",
                    callback=src.infos.update_displayed_courses
                )
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text("选择对应的学院~~\n如果没有选默认就好辣！")
            with dpg.group(horizontal=True):
                dpg.add_text("专业模板：")
                dpg.add_combo(
                    items=src.infos.get_courses_from_school(),
                    source="selected_major",
                    tag="Selected_major"
                )
            with dpg.group(horizontal=True):
                dpg.add_text("保存周次：")
                dpg.add_input_int(source="selected_week")

            with dpg.group(horizontal=True):
                _dir_select = dpg.add_file_dialog(
                    directory_selector=True,
                    show=False,
                    callback=utils.store_selected_saving_path
                )
                dpg.add_button(label="保存位置", callback=lambda: dpg.show_item(_dir_select))
                dpg.add_text(tag="disp-dir-1", default_value="")

            with dpg.group(horizontal=True):
                dpg.add_text("输出格式:")
                dpg.add_radio_button(("ics", "txt", "csv"), horizontal=True)

        dpg.add_button(label="开始！ bui~", callback=StartProcess)

        dpg.bind_font(font)

    dpg.create_viewport(title='SWJTU Calendar', width=900, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    dpg.set_primary_window(main, True)

    dpg.start_dearpygui()
    dpg.destroy_context()
