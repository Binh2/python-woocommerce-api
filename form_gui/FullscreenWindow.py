from tkinter import *


class FullscreenWindow:
  def __init__(self, tk: Tk):
    self.tk = tk
    self.tk.state('zoomed')
    # self.__frame = Frame(self.tk)
    # self.__frame.pack()
    self.__state = True
    self.tk.bind("<F11>", self.toggle_fullscreen)
    self.tk.bind("<Escape>", self.end_fullscreen)

  def toggle_fullscreen(self, event=None):
    self.__state = not self.__state  # Just toggling the boolean
    self.tk.attributes("-fullscreen", self.__state)
    return "break"

  def end_fullscreen(self, event=None):
    self.__state = False
    self.tk.attributes("-fullscreen", False)
    return "break"

if __name__ == '__main__':
  w = FullscreenWindow(Tk())
  w.tk.mainloop()