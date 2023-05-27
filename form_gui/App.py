from tkinter import *
from typing import Callable, List
from FullscreenWindow import FullscreenWindow
from ScrollableWindow import ScrollableWindow
from string import ascii_uppercase


class App(FullscreenWindow, ScrollableWindow):
  def __init__(self, tk: Tk, column_names: List[str], insert: Callable = None, **kwargs):
    super(ScrollableWindow).__init__(tk)
    super(FullscreenWindow).__init__(tk)
    self.tk = tk
    self.tk.title('Product')
    self.column_names = column_names
    self.insert: Callable = insert
    self.labels: List[Label] = []
    self.fields: List[Entry] = []
    self.OVERFLOW = 25
    # self.create_textbox(Frame(self.tk))
    frame = Frame(self.tk)
    frame.pack()
    self.add_fields(frame)
    # self.add_submit(frame)

  def add_fields(self, frame: Frame):
    for index, column_name in zip(range(1, 10000), self.column_names):
      label = Label(frame, text=column_name, bg='light green')
      label.grid(row=index % self.OVERFLOW, column=0 + (index // self.OVERFLOW) * 2)
      self.labels.append(label)

      field = Entry(frame)
      field.bind('<Return>', lambda: field.focus_set())
      field.grid(row=index % self.OVERFLOW, column=1 + (index // self.OVERFLOW) * 2, ipadx="100")
      self.fields.append(field)

  def add_submit(self, frame: Frame):
    submit = Button(frame, text="Submit", fg="Black",
              bg="Red", command=lambda: self.insert(self.fields))
    submit.grid(row=self.OVERFLOW + 2, column=1)

  def create_textbox(self, frame: Frame, height = 10, width = 15):
    frame.pack()
    self.textbox = Text(frame, height = height, width = width, wrap = 'word')
    vertscroll = Scrollbar(frame)
    vertscroll.config(command=self.textbox.yview)
    self.textbox.config(yscrollcommand=vertscroll.set)
    self.textbox.grid(column=0, row=0)
    vertscroll.grid(column=1, row=0, sticky='NS')
    return frame
  
  def focus(field: Entry):
    field.focus_set()

  def clear_form(self):
    for field in self.fields:
      field.delete(0, END)

if __name__ == "__main__":
  root = App(Tk())
  root.tk.mainloop()