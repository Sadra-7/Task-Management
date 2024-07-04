from ttkbootstrap import *

class Welcome(Frame):
    def __init__(self , view , window):
        super().__init__(window)
        self.grid_columnconfigure(0 , weight=1)

        self.view = view

        self.title = Label(self , text="Welcome to task manager application" , bootstyle = DEFAULT)
        self.title.grid(row = 0 , column = 0 , padx=  10 , pady = 10)

        self.login = Button(self , text="LOGIN",  bootstyle = "success-outline" , command=self.login_clicked)
        self.login.grid(row = 1 , column = 0, padx=  10 , pady = 10, sticky = "ew" )

        self.create_account = Button(self , text="CREATE ACCOUNT", bootstyle = "WARNING-OUTLINE" , command=self.create_account_clicked)
        self.create_account.grid(row = 2 , column = 0, padx=  10 , pady = 10, sticky = "ew")


    def login_clicked(self):
        self.view.switch("login")

    def create_account_clicked(self):
        self.view.switch("create")