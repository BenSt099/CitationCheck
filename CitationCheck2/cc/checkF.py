from customtkinter import CTkFrame

class CHECK_FRAME(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.configure(fg_color='red')
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        # self.grid_rowconfigure(5, weight=1)
        # self.grid_rowconfigure(6, weight=1)
        # self.grid_rowconfigure(7, weight=1)
        # self.grid_columnconfigure(0, weight=1)