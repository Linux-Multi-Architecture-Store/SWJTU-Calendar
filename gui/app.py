import dearpygui.dearpygui as dpg
import gui.utils as utils

def new_window():
    with dpg.window(label="New"):
        dpg.add_button(label="Hello!")


def App():
    dpg.create_context()

    font = utils.add_fonts_and_dpi("assets/fonts/PingFang.ttf", 1.5)

    with dpg.window(label="Tutorial"):
        b0 = dpg.add_button(label="New Windows", callback=new_window)
        b1 = dpg.add_button(tag=100, label="Button 1")
        dpg.add_button(tag="Btn2", label="Button 2")
        dpg.bind_font(font)

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
