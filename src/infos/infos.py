import dearpygui.dearpygui as dpg

APP_VERSION = "V2.0.0.20221110_beta"

SUPPORTED_SCHOOL = [
    "默认",
    "利兹学院"
]

SUPPORTED_MAJORS = {
    "默认": ["默认"],
    "利兹学院": ["电子信息工程"]
}


def get_courses_from_school():
    _selected_school = dpg.get_value("selected_school")
    _majors = SUPPORTED_MAJORS.get(_selected_school, ["默认"])
    return _majors


def update_displayed_courses():
    dpg.configure_item("Selected_major", items=get_courses_from_school())
