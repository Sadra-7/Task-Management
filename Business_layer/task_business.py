from Task_management.DataAcces_layer.task_data import User_data
from Task_management.Common_layer.entry_chek import EntryDescriptor
from Task_management.Common_layer.date_check import Date
from Task_management.Common_layer.user_descriptor import UserDescriptor
from datetime import date

class User_business:
    date_now = date.today()
    username = UserDescriptor(3)
    password = UserDescriptor(3)
    name = EntryDescriptor(3 , "Name")
    detail = EntryDescriptor(8 , "Detail")
    date_date = Date()



    def __init__(self):
        self.data_access = User_data()

    def login(self , username , password):
        try:
            self.username = username
            self.password = password
        except:
            return (None , "Invalid value username or password")

        user = self.data_access.check_user(username , password)
        if user:
            return (user,None)
        else:
            return None, ("Incorrent username or password")

    def load_task(self, user_id):
        task = self.data_access.load_task_data(user_id)
        if task:
            return (task , None)
        else:
            return (None , "you do not have any task!")
    def new_account(self , firstname , username , password):


        user = self.data_access.add_user(firstname , username , password)

        if user:
            return (user , None)

        else:
            return (None , "error")

    def new_task(self , name , detail , date1 , user_id):

        self.name = name
        self.detail = detail


        try:
            self.date_date = date1
            new_date = date.fromisoformat(self.date_date)
            if new_date < self.date_now:
                return (None , "Invalid date")
            else:
                self.data_access.add_task(self.name , self.detail , self.date_date , user_id)
                return ("a" , None)

        except:
            return (None, None)

    def get_task(self, task_id):
        task = self.data_access.show_task_data(task_id)
        return task

    def edit_task(self,task_id , name , date1 , detail , complete):
        try:
            self.date_date = date1
            new_date = date.fromisoformat(self.date_date)
            if new_date < self.date_now:
                return (None , "Invalid date")
            else:
                self.new_task = self.data_access.edit_task_data(task_id , name , detail , self.date_date , complete)
                return ("a" , None)

        except:
            return self.new_task , None

    def delete_task(self,task_id):
        self.data_access.delete_task_data(task_id)

    def done_task(self,id , condition , complete):
        task = self.data_access.change_condition_data(id , condition , complete)
        return task

    def search(self , condition , id):
        task = self.data_access.search_data(condition , id)
        if task:
            return (task , None)

        else:
            return (None,"Error\nPlese Reset")

    def sort_title_business(self , title , id):

        result = self.data_access.sort_data_title(title , id)
        if result:
            return (result , None)
        else:
            return (None , "error")
    def sort_complete_business(self , percent , id):
        result = self.data_access.sort_data_complete(percent , id)
        if result:
            return (result , None)
        else:
            return (None , "error")

