from ttkbootstrap import *

class Show(Frame):
    def __init__(self , view , window):
        super().__init__(window)

        self.view = view

        self.grid_columnconfigure(1 , weight=1)

        self.id_label = Label(self, text="DATA BASE ID :")
        self.id_label.grid(row=2, column=0, padx=10, pady=10)

        self.name_label = Label(self, text="Name :")
        self.name_label.grid(row=3, column=0, padx=10, pady=10)

        self.detail_label = Label(self, text="Detail :")
        self.detail_label.grid(row=4, column=0, padx=10, pady=10)

        self.date_label = Label(self, text="Date :")
        self.date_label.grid(row=5, column=0, padx=10, pady=10)

        self.condition_label = Label(self, text="Condition :")
        self.condition_label.grid(row=6, column=0, padx=10, pady=10)





        self.id_entry = Entry(self, width=10, bootstyle = INFO)
        self.id_entry.grid(row=2, column=1, padx=10, pady=10 , sticky = "ew")

        self.name_entry = Entry(self, width=10, bootstyle = INFO)
        self.name_entry.grid(row=3, column=1, padx=10, pady=10, sticky = "ew")

        self.detail_entry = Entry(self, width=100, bootstyle = INFO)
        self.detail_entry.grid(row=4, column=1, padx=10, pady=10, sticky = "ew")

        self.date_entry = Entry(self, width=10, bootstyle = INFO)
        self.date_entry.grid(row=5, column=1, padx=10, pady=10, sticky = "ew")

        self.condition_entry = Entry(self, width=10 , bootstyle = INFO)
        self.condition_entry.grid(row=6, column=1, padx=10, pady=10, sticky = "ew")

        self.edit_button = Button(self, text="EDIT", command=self.edit_clicked, bootstyle =" WARNING-OUTLINE")
        self.edit_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

        self.back = Button(self, text="BACK", command=self.back_clicked, bootstyle =" DANGER-OUTLINE")
        self.back.grid(row=7, column=0, padx=10, pady=10, sticky="ew")






    def get_current_task(self,task):

        self.id_entry.insert(0 , task.task_id)
        self.name_entry.insert(0 , task.name)
        self.detail_entry.insert(0 , task.detail)
        self.date_entry.insert(0 , task.finish_date)
        self.condition_entry.insert(0 , "Done" if task.condition == 1 else "In Progress")
        self.complete = int(task.complete)

        self.meter = Meter(self , metersize=200 ,  amountused=self.complete , metertype=FULL ,subtext="Done" , textright="%" , stripethickness=10 , bootstyle=INFO , subtextstyle=INFO)
        self.meter.grid(row=1,rowspan = 10 ,  column=2, padx=10, pady=10, sticky = "ew")

    def back_clicked(self):
        self.id_entry.delete(0 , END)
        self.name_entry.delete(0 , END)
        self.detail_entry.delete(0 , END)
        self.date_entry.delete(0 , END)
        self.condition_entry.delete(0 , END)

        self.view.switch("home")



    def get_user(self , user_id):
        self.user = user_id

    def edit_clicked(self):



        edit = self.view.switch("edit")
        edit.get_id(self.id_entry.get() , self.user)

        edit.get_data_task(self.name_entry.get(), self.detail_entry.get(), self.date_entry.get(), self.complete)
        self.id_entry.delete(0 , END)
        self.name_entry.delete(0 , END)
        self.detail_entry.delete(0 , END)
        self.date_entry.delete(0 , END)
        self.condition_entry.delete(0 , END)






