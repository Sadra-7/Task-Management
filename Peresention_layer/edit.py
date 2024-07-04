from ttkbootstrap import *
from ttkbootstrap.dialogs import Messagebox
from Task_management.Common_layer.entry_chek import EntryDescriptor
from Task_management.Common_layer.date_check import Date

from Task_management.Business_layer.task_business import User_business

class Edit(Frame):

    new_name = EntryDescriptor(3  , "Name")
    new_detail = EntryDescriptor(8 , "Detail")
    new_date = Date()



    def __init__(self , view , window):
        super().__init__(window)

        self.business = User_business()

        self.view = view

        self.grid_columnconfigure(1 , weight=1)

        self.name_label = Label(self, text="Name :")
        self.name_label.grid(row=2, column=0, padx=10, pady=10)

        self.detail_label = Label(self, text="Detail :")
        self.detail_label.grid(row=3, column=0, padx=10, pady=10)

        self.date_label = Label(self, text="Date :")
        self.date_label.grid(row=4, column=0, padx=10, pady=10)


        self.complete_label = Label(self, text="Complete :")
        self.complete_label.grid(row=6, column=0, padx=10, pady=10)

        self.name_entry = Entry(self, width=10, bootstyle=INFO)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.detail_entry = Entry(self, width=100, bootstyle=INFO)
        self.detail_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.date_entry = Entry(self, width=10, bootstyle=INFO)
        self.date_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")


        self.complete_entry = Entry(self, width=10, bootstyle=INFO)
        self.complete_entry.grid(row=6, column=1, padx=10, pady=10, sticky="ew")


        self.save_button = Button(self, text="SAVE", command=self.save_clicked, bootstyle =" WARNING-OUTLINE")
        self.save_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

        self.back = Button(self, text="BACK", command=self.back_clicked, bootstyle =" DANGER-OUTLINE")
        self.back.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

    def back_clicked(self):
        home = self.view.switch("home")
        home.load_data_task()

        self.name_entry.delete(0, END)
        self.detail_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.complete_entry.delete(0, END)


    def get_id(self , task_id , user_id):
        self.task_id = task_id
        self.user_id = user_id

    def get_data_task(self , name , detail , date , complete):
        self.name= name
        self.detail = detail
        self.date = date
        self.complete = complete


        self.name_entry.insert(0, self.name)
        self.detail_entry.insert(0, self.detail)
        self.date_entry.insert(0, self.date)
        self.complete_entry.insert(0 , self.complete)

    def save_clicked(self):

        self.new_name = self.name_entry.get()
        self.new_detail = self.detail_entry.get()
        self.new_date = self.date_entry.get()
        self.new_complete = self.complete_entry.get()

    @property
    def new_complete(self):
        return self._complete

    @new_complete.setter
    def new_complete(self,value):


        try:
            int(value)

        except:
            Messagebox.show_error(title="ERROR!", message="Invalid value(you cant use word in complete!)")
            value = None

        if len(value) <=3:
            self._complete = value
        else:
            Messagebox.show_error(title="ERROR!", message="Invalid value(complete name 3 digit!)")




        if self.new_name and self.new_detail and self.date and self._complete:
            result = self.business.edit_task(self.task_id , self.new_name , self.new_date , self.new_detail , self._complete)
            error = result[1]
            task = result[0]
            if task:
                if self._complete != "100":
                    self.business.done_task(self.task_id , 0 , self._complete)
                Messagebox.show_info(title="TASK EDITED", message="YOUR TASK EDITED!")
            elif error == "Invalid date":
                Messagebox.show_error(title="Error" , message="Please change your date!")








