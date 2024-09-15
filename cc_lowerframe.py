from customtkinter import CTkFont
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkFrame
from customtkinter import CTkImage
from customtkinter import get_appearance_mode
from PIL import Image
from webbrowser import open_new

###############################################################################################
#####################################      LOWERFRAME     #####################################
###############################################################################################
class LowerFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        if get_appearance_mode() == 'Light':
            textcolor = "black"
            hovercolor = "#d9d8d7"
            colorFrame = "#d9d8d7"
        else:
            colorFrame = "gray13"
            textcolor = "white"
            hovercolor = "#181818" 

        self.configure(fg_color=colorFrame)

        innerFrame = CTkFrame(master=self, height=20, fg_color=colorFrame)
        innerFrame.grid(row=0, column=0, padx=160, pady=10, sticky="ew")
        innerFrame.grid_rowconfigure(0, weight=1)
        innerFrame.grid_rowconfigure(1, weight=1)
        innerFrame.grid_columnconfigure(0, weight=1)

        upperFrame = CTkFrame(master=innerFrame, fg_color=colorFrame)
        lowerFrame = CTkFrame(master=innerFrame, fg_color=colorFrame)
        upperFrame.grid(row=0, column=0, sticky="ew")
        lowerFrame.grid(row=1, column=0, sticky="ew")

        upperFrame.grid_rowconfigure(0, weight=1)
        upperFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_rowconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(1, weight=1)

        label = CTkLabel(upperFrame, text="CitationCheck v1.0", height=10, font=CTkFont(family='times new roman 16 bold', size=16, weight="bold"))
        label.grid(row=0, column=0, padx=0, pady=0, sticky="ew")           

        image_github = CTkImage(Image.open("logo_github.png"), size=(18,18))
        label_github = CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color=hovercolor, text_color=textcolor, text="Homepage", image=image_github, compound="left", font=CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHub)
        label_github.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image_issue = CTkImage(Image.open("issue.png"), size=(18,18))
        label_issue = CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color=hovercolor, text_color=textcolor, text="Issues", image=image_issue, compound="left", font=CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHubIssue)
        label_issue.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

    def openGitHub(self):
        open_new(r"https://github.com/BenSt099/CitationCheck")

    def openGitHubIssue(self):
        open_new(r"https://github.com/BenSt099/CitationCheck/issues")

###############################################################################################
#####################################      LOWERFRAME     #####################################
###############################################################################################