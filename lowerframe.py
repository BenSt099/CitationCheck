import customtkinter
from PIL import Image
import webbrowser

###############################################################################################
#####################################      LOWERFRAME     #####################################
###############################################################################################
class LowerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        innerFrame = customtkinter.CTkFrame(master=self, height=20)
        innerFrame.grid(row=0, column=0, padx=160, pady=10, sticky="ew")
        innerFrame.grid_rowconfigure(0, weight=1)
        innerFrame.grid_rowconfigure(1, weight=1)
        innerFrame.grid_columnconfigure(0, weight=1)

        upperFrame = customtkinter.CTkFrame(master=innerFrame)
        lowerFrame = customtkinter.CTkFrame(master=innerFrame)
        upperFrame.grid(row=0, column=0, sticky="ew")
        lowerFrame.grid(row=1, column=0, sticky="ew")

        upperFrame.grid_rowconfigure(0, weight=1)
        upperFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_rowconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(1, weight=1)

        label = customtkinter.CTkLabel(upperFrame, text="CitationCheck v1.0", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=16, weight="bold"))
        label.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image_github = customtkinter.CTkImage(Image.open("logo_github.png"), size=(18,18))
        label_github = customtkinter.CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color="#181818", text="Homepage", image=image_github, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHub)
        label_github.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image_issue = customtkinter.CTkImage(Image.open("issue.png"), size=(18,18))
        label_issue = customtkinter.CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color="#181818", text="Issues", image=image_issue, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHubIssue)
        label_issue.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

    def openGitHub(self):
        webbrowser.open_new(r"https://github.com/BenSt099/CitationCheck")

    def openGitHubIssue(self):
        webbrowser.open_new(r"https://github.com/BenSt099/CitationCheck/issues")
