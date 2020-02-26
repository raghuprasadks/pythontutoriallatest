import tkinter as tk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("The Root class with menu")
        self.a_frame = FrameWithMenu(self)
        self.create_menu()

    def create_menu(self):
        self.menubar = tk.Menu(self)
        self.menubar.add_command(label="Root", command=self.a_frame.replace_menu)
        self['menu'] = self.menubar



class FrameWithMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def replace_menu(self):
        """ Overwrite parent's menu if parent's class name is in _valid_cls_names.
        """

        _parent_cls_name = type(self.master).__name__
        _valid_cls_names = ("Tk", "Toplevel", "Root")
        if _parent_cls_name in _valid_cls_names:
            self.menubar = tk.Menu(self)
            self.menubar.add_command(label="Frame", command=self.master.create_menu)
            self.master['menu'] = self.menubar


if __name__ == '__main__':
    root = Root()
    root.mainloop()