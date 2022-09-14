import sys
import tkinter as tk
from gui.app import MainApp

sys.setrecursionlimit(2147483647)

root = tk.Tk()
root.title("SWJTU课表导出日历小工具")
app = MainApp(root)
root.mainloop()