import dearpygui.dearpygui as dpg


def store_selected_saving_path(sender, app_data):
    dpg.set_value("selected_saving_path", app_data['file_path_name'])
    dpg.configure_item("disp-dir-1", default_value=app_data['file_path_name'])