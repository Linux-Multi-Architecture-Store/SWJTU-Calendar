import dearpygui.dearpygui as dpg


def add_fonts_and_dpi(font_path, scale) -> ...:
    with dpg.font_registry():
        with dpg.font(font_path, 20 * scale) as font1:
            # add the default font range
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

            # helper to add range of characters
            #    Options:
            #        mvFontRangeHint_Japanese
            #        mvFontRangeHint_Korean
            #        mvFontRangeHint_Chinese_Full
            #        mvFontRangeHint_Chinese_Simplified_Common
            #        mvFontRangeHint_Cyrillic
            #        mvFontRangeHint_Thai
            #        mvFontRangeHint_Vietnamese
    return font1
