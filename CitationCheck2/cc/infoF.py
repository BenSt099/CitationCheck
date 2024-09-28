from customtkinter import CTkFrame
from customtkinter import CTkTextbox
from customtkinter import CTkLabel
from customtkinter import CTkFont

class INFO_FRAME(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.configure(fg_color='#101221')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        l_heading = CTkLabel(self, text="Information", text_color="white", font=CTkFont(family='times new roman 14 bold', size=38, weight="bold"))
        l_heading.grid(row=0, column=0, padx=0 ,sticky="new")

        l_heading = CTkLabel(self, text="CitationCheck - Validate your references!", text_color="white", font=CTkFont(family='times new roman 14', slant="italic", size=22))
        l_heading.grid(row=1, column=0, padx=0 ,sticky="new")

        l_heading = CTkLabel(self, text="This is CitationCheck, version v1.0.", text_color="white", font=CTkFont(family='times new roman 14', size=20))
        l_heading.grid(row=2, column=0, padx=0 ,sticky="new")

        textbox = CTkTextbox(self, fg_color='#101221', height=150, font=CTkFont(family='times new roman 14', size=18))
        textbox.insert("0.0", "The purpose of this project is to validate your references by using the data from Crossref and RetractionWatch. While this project was created with the utmost care, errors and problems can still arise. Therefore, this project and all reports generated with it come WITHOUT ANY WARRANTY, without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.")
        textbox.configure(state="disabled")
        textbox.grid(row=3, column=0, padx=20, sticky="ew")

        p1 = CTkFrame(master=self)
        p1.configure(fg_color='#101221')
        p1.grid(row=4, column=0, sticky="ew")

        p1.grid_columnconfigure(0, weight=1)
        p1.grid_rowconfigure(0, weight=1)
        p1.grid_rowconfigure(1, weight=1)
        p1.grid_rowconfigure(2, weight=1)

        t1 = CTkLabel(p1, text="This project is licensed under GNU General Public License v3.0.", fg_color='#101221', text_color="white", font=CTkFont(family='times new roman 14', slant="italic", size=18))
        t1.grid(row=0, column=0, padx=0 ,sticky="new")

        t2 = CTkLabel(p1, text="For more information, please visit the homepage of this project, which you can view at:", fg_color='#101221', text_color="white", font=CTkFont(family='times new roman 14', size=18))
        t2.grid(row=1, column=0, padx=0 ,sticky="new")

        p2 = CTkFrame(master=p1)
        p2.configure(fg_color='#101221')
        p2.grid(row=3, column=0, sticky="ew")
        p2.grid_columnconfigure(0, weight=1)
        p2.grid_columnconfigure(1, weight=1)
        p2.grid_columnconfigure(2, weight=1)
        p2.grid_rowconfigure(0, weight=1)

        t3 = CTkTextbox(p2, fg_color='#101221', height=8, font=CTkFont(family='times new roman 14', size=18))
        t3.insert("0.0", "     https://github.com/BenSt099/CitationCheck     ")
        t3.configure(state="disabled")
        t3.grid(row=0, column=1, padx=20, sticky="ew")

        p3 = CTkFrame(master=self)
        p3.configure(fg_color='#101221')
        p3.grid(row=5, column=0, sticky="ew")

        p3.grid_columnconfigure(0, weight=1)
        p3.grid_rowconfigure(0, weight=1)
        p3.grid_rowconfigure(1, weight=1)
        p3.grid_rowconfigure(2, weight=1)

        t4 = CTkLabel(p3, text="If you would like to report a bug, a feature or run into an issue, you can create an issue on GitHub:", fg_color='#101221', text_color="white", font=CTkFont(family='times new roman 14', size=18))
        t4.grid(row=1, column=0, padx=0 ,sticky="new")

        p4 = CTkFrame(master=p3)
        p4.configure(fg_color='#101221')
        p4.grid(row=3, column=0, sticky="ew")
        p4.grid_columnconfigure(0, weight=1)
        p4.grid_columnconfigure(1, weight=1)
        p4.grid_columnconfigure(2, weight=1)
        p4.grid_rowconfigure(0, weight=1)

        t5 = CTkTextbox(p4, fg_color='#101221', height=8, font=CTkFont(family='times new roman 14', size=18))
        t5.insert("0.0", "https://github.com/BenSt099/CitationCheck/issues")
        t5.configure(state="disabled")
        t5.grid(row=0, column=1, padx=2, sticky="ew")