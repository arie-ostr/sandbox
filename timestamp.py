from tkinter import Tk
from time import gmtime, strftime
timestr = strftime("%Y-%m-%d %H:%M:%S", gmtime())

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(timestr)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
