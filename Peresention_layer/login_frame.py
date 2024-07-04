from ttkbootstrap import *
from ttkbootstrap.dialogs import Messagebox
from Task_management.Business_layer.task_business import User_business


class Login_fram(Frame):
    def __init__(self ,view ,  window):
        super().__init__(window)

        self.view = view

        self.business_task = User_business()

        self.grid_columnconfigure(1 , weight=1)


        self.username_label = Label(self , text="Username : ")
        self.username_label.grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "e")

        self.username_entry = Entry(self , width=20 , bootstyle = INFO)
        self.username_entry.grid(row = 1 , column = 1 , padx = 10 , pady = 10 , sticky = "ew" )
        self.username_entry.insert(0 , "s.amini")

        self.password_label = Label(self , text="Password : " )
        self.password_label.grid(row= 2 , column = 0 , padx = 10 , pady = 10 , sticky = "e")

        self.password_entry = Entry(self , width=20 , bootstyle = INFO )
        self.password_entry.grid(row = 2  , column = 1 ,padx = 10 , pady =10 , sticky = "ew" )
        self.password_entry.insert(0 , "123")

        self.login_button = Button(self , text="DONE" , bootstyle = "SUCCESS-OUTLINE" , command=self.login_clicked)
        self.login_button.grid(row= 3 , column= 1 , padx = 10 , pady = 10 , sticky = "ew")

        self.back = Button(self , text="BACK" , bootstyle = "DANGER-OUTLINE" , command=self.back_clicked)
        self.back.grid(row= 3 , column= 0 , padx = 10 , pady = 10 , sticky = "ew")


    def login_clicked(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.business_task.login(username , password)




        error = user[1]
        self.result_user = user[0]





        if error:
            Messagebox.show_error(title="ERROR!" , message=error)

        else:

            home = self.view.switch("home")
            home.current_user(self.result_user)
            home.load_data_task()






    def back_clicked(self):
        self.view.switch("welcome")





