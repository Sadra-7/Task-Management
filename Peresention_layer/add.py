from ttkbootstrap import *
from Task_management.Common_layer.entry_chek import EntryDescriptor
from Task_management.Common_layer.date_check import Date
from Task_management.Business_layer.task_business import User_business
from ttkbootstrap.dialogs import Messagebox


class Add(Frame):

    def __init__(self, view , window):

        super().__init__(window)

        self.business = User_business()

        self.view = view

        self.grid_columnconfigure(1 , weight=1)

        self.title = Label(self , text="ADD NEW TASK")
        self.title.grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        self.name_label = Label(self ,text="Name :")
        self.name_label.grid(row = 1 , column = 0 , padx = 10 , pady = 10)

        self.detail_label = Label(self ,text="Detail :")
        self.detail_label.grid(row = 2 , column = 0 , padx = 10 , pady = 10)

        self.date_label = Label(self ,text="Date :")
        self.date_label.grid(row = 3 , column = 0 , padx = 10 , pady = 10)




        self.name_entry = Entry(self ,width=20 , bootstyle = INFO)
        self.name_entry.grid(row = 1 , column = 1 , padx = 10 , pady = 10 , sticky = "ew")

        self.detail_entry = Entry(self ,width=100, bootstyle = INFO)
        self.detail_entry.grid(row = 2 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

        self.date_entry = Entry(self ,width=20, bootstyle = INFO)
        self.date_entry.grid(row = 3 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

        self.back = Button(self , text="BACK" , bootstyle ="DANGER-OUTLINE" , command=self.back_clicked)
        self.back.grid(row = 4, column = 0, padx = 10 , pady = 10, sticky = "ew")

        self.add_account = Button(self , text="ADD TASK" , bootstyle ="SUCCESS-OUTLINE" , command=self.add_task_clicked)
        self.add_account.grid(row = 4 , column = 1 , padx = 10 , pady = 10, sticky = "ew")

    def back_clicked(self):


        home = self.view.switch("home")
        home.load_data_task()

        self.name_entry.delete(0 , END)
        self.detail_entry.delete(0, END)
        self.date_entry.delete(0, END)



    def get_id(self, user_id):
        self.user = user_id
        self.user_id = user_id

    def add_task_clicked(self):

        self.name = self.name_entry.get()
        self.detail = self.detail_entry.get()
        self.date = self.date_entry.get()

        result = self.business.new_task(self.name , self.detail , self.date , self.user_id)
        task = result[0]
        error = result[1]
        if task:
            Messagebox.show_info(title="TASK ADDED", message="YOUR TASK SAVED!")
            home = self.view.switch("home")
            home.load_data_task()
            self.name_entry.delete(0, END)
            self.detail_entry.delete(0, END)
            self.date_entry.delete(0, END)
        elif error == "Invalid date":
            Messagebox.show_error(title="Error" , message="Please change your date")












