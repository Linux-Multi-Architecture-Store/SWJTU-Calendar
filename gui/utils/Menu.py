import dearpygui.dearpygui as dpg
from .Windows import about_programme
from .extras import exit_programme


def add_menu():
    with dpg.menu_bar() as menubar:
        """"""
        """
        with dpg.menu(label="Themes"):
            dpg.add_menu_item(label="Dark")
            dpg.add_menu_item(label="Light")
            dpg.add_menu_item(label="Classic")

            with dpg.menu(label="Other Themes"):
                dpg.add_menu_item(label="Purple")
                dpg.add_menu_item(label="Gold")
                dpg.add_menu_item(label="Red")

        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Show Logger")
            dpg.add_menu_item(label="Show About")

        with dpg.menu(label="Oddities"):
            dpg.add_button(label="A Button")
            dpg.add_simple_plot(label="Menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80)
        """
        with dpg.menu(label="文件"):
            dpg.add_button(label="退出", callback=exit_programme)

        dpg.add_separator()

        with dpg.menu(label="帮助"):
            dpg.add_button(label="关于", callback=about_programme)

            dpg.add_separator()

            dpg.add_button(label="开发者工具", callback=lambda: dpg.show_item_registry())

    return menubar
