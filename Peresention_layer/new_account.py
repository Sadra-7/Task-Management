from ttkbootstrap import *
from Task_management.Business_layer.task_business import User_business
from Task_management.Common_layer.entry_chek import EntryDescriptor
from ttkbootstrap.dialogs import Messagebox

class Create(Frame):

    username = EntryDescriptor(5 , "Username")
    password = EntryDescriptor(3 , "Password")
    def __init__(self , view , window):
        super().__init__(window)

        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        self.view = view

        self.business = User_business()

        self.grid_columnconfigure(1 , weight=1)

        self.title = Label(self , text="CREATE ACCOUNT")
        self.title.grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        self.first_name_label = Label(self , text = "First name :")
        self.first_name_label.grid(row = 1 , column = 0 , padx = 10 , pady = 10)

        self.username_label = Label(self , text = "Username :")
        self.username_label.grid(row = 2 , column = 0 , padx = 10 , pady = 10)

        self.password_label = Label(self , text = "Password :")
        self.password_label.grid(row = 3 , column = 0 , padx = 10 , pady = 10)




        self.first_name_entry = Entry(self , width=20 , bootstyle = INFO)
        self.first_name_entry.grid(row = 1 , column = 1 , padx = 10 , pady = 10 , sticky = "ew")

        self.username_entry = Entry(self , width=20 , bootstyle = INFO)
        self.username_entry.grid(row = 2 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

        self.password_entry = Entry(self , width=20 , bootstyle = INFO)
        self.password_entry.grid(row = 3 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

        self.back = Button(self , text="BACK" , bootstyle ="DANGER-OUTLINE" , command=self.back_clicked)
        self.back.grid(row = 4, column = 0 , padx = 10 , pady = 10, sticky = "ew")

        self.add_account = Button(self , text="ADD ACCOUNT" , bootstyle ="SUCCESS-OUTLINE" , command=self.add_account_clicked)
        self.add_account.grid(row = 4 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

    def back_clicked(self):
        self.view.switch("welcome")
        self.first_name_entry.delete(0 , END)
        self.username_entry.delete(0 , END)
        self.password_entry.delete(0 , END)

    def add_account_clicked(self):
        self.firstname = self.first_name_entry.get()

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        for i in value:
            if i in self.numbers:
                Messagebox.show_error(title="ERROR!", message="Invalid value(you cant use number in  first name!)")
                value = None
                break

        if len(value) < 3:
            Messagebox.show_error(title="ERROR!",message="Invalid value(Invalid value(first name 3 digit)")
            value = None


        self._firstname = value
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        if self.firstname and self.username and self.password:


            self.business.new_account(self._firstname, self.username , self.password)

            Messagebox.show_info(title="ACCOUNT ADDED" , message="YOUR ACCOUNT SAVED!")
            self.first_name_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)




