from tkinter import *


class ScrollableWindow():
  def __init__(self, tk: Tk):
    self.tk = tk
    scrollbar = Scrollbar(self.tk)
    scrollbar.pack( side = RIGHT, fill = Y )
