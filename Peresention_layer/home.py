from ttkbootstrap import *
from ttkbootstrap.dialogs import Messagebox
from Task_management.Business_layer.task_business import User_business

class Home(Frame):
    def __init__(self ,view ,  window):
        super().__init__(window)

        self.view = view

        self.task_item = []

        value = ["Done" , "InProgress" , "Reset"]
        value_sort = ["Title", "Most Complete Percent", "Reset"]

        self.combobox = Combobox(self , values=value , bootstyle = PRIMARY)
        self.combobox.grid(row=1, column=0, padx=10, pady=10)
        self.combobox.insert(0 , "Reset")

        self.combobox_sort = Combobox(self , values=value_sort , bootstyle = PRIMARY)
        self.combobox_sort.grid(row=1, column=1, padx=10, pady=10)
        self.combobox_sort.insert(0 , "Reset")

        self.search_button = Button(self, text="SEARCH", command=self.load_data_task, bootstyle ="PRIMARY-OUTLINE")
        self.search_button.grid(row=2, column=0, padx=10, pady=10)

        self.sort_button = Button(self, text="SORT", command=self.load_data_task, bootstyle="PRIMARY-OUTLINE")
        self.sort_button.grid(row=2, column=1, padx=10, pady=10)

        self.done = Button(self, text="DONE", command=self.done_clicked, bootstyle =" SUCCESS-OUTLINE")
        self.done.grid(row=5, column=0,columnspan =2, padx=10, pady=10, sticky="ew")

        self.add_button = Button(self, text="ADD TASK" , command=self.add_button_clicked , bootstyle =" INFO-OUTLINE")
        self.add_button.grid(row=  6 , column = 0,columnspan =2 , padx = 10 , pady = 10  , sticky = "ew")

        self.show_button = Button(self, text="TASK INFO AND EDIT" , command=self.show_task, bootstyle =" INFO-OUTLINE")
        self.show_button.grid(row =7, column = 0,columnspan =2 , padx = 10 , pady = 10 , sticky = "ew")



        self.delete_button = Button(self, text="DELETE", command=self.delete, bootstyle =" WARNING-OUTLINE")
        self.delete_button.grid(row=8,columnspan =2 , column=0, padx=10, pady=10, sticky="ew")

        self.back = Button(self, text="BACK", command=self.back_clicked, bootstyle =" DANGER-OUTLINE")
        self.back.grid(row=9, column=0,columnspan =2, padx=10, pady=10, sticky="ew")


        self.business = User_business()

        self.title_label = Label(self , text="Welcome")
        self.title_label.grid(row = 0 , column = 0 , padx = 10 , pady = 10, columnspan = 4)
        self.grid_columnconfigure(0 , weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4 , weight=1)

        self.column = ["name" , "detail" ,"start_date", 'finish_date' , 'condition' , 'complete']

        self.table = Treeview(self , columns=self.column , bootstyle = INFO )

        self.table.heading(column="#0" , text="NO")
        self.table.heading(column="name", text="Name")
        self.table.heading(column="detail", text="Detail")
        self.table.heading(column="start_date", text="You start at...")
        self.table.heading(column="finish_date", text="You want finish at...")
        self.table.heading(column="condition", text="Condition")
        self.table.heading(column="complete", text="Complete")

        self.table.grid(row = 4 , column = 0 , padx= 10 , pady = 10 , sticky = "nsew", columnspan = 4)




    def current_user(self , user):
        self.current_user_name = user
        self.title_label.config(text=f"Welcome {user.firstname}")

    def reset_combobox(self):
        self.combobox.delete(0, END)
        self.combobox.insert(0 , "Reset")

    def reset_combobox_sort(self):
        self.combobox_sort.delete(0, END)
        self.combobox_sort.insert(0 , "Reset")

    def load_data_task(self):
        self.result = None

        search_data = self.combobox.get()
        sort_data = self.combobox_sort.get()
        self.current_id = self.current_user_name.id
        self.result = self.business.load_task(self.current_id)

        if search_data == "Reset":
            self.result = self.business.load_task(self.current_id)
            if sort_data == "Title":
                self.result = self.sort_title()
            elif sort_data == "Most Complete Percent":
                self.result = self.sort_persent()
        else:
            if sort_data != "Reset":
                self.reset_combobox_sort()
                Messagebox.show_error(title="Error", message="You cant use (SEARCH and SORT) in one time\nplease click on both buttons to reset and try again!")
        if sort_data == "Reset":
            self.result = self.business.load_task(self.current_id)
            if search_data == "InProgress":
                self.result = self.business.search(0, self.current_id)
            elif search_data == "Done":
                self.result = self.business.search(1, self.current_id)
        else:
            if search_data != "Reset":
                self.reset_combobox()
                Messagebox.show_error(title="Error" , message="You cant use (SEARCH and SORT) in one time\nplease click on both buttons to reset and try again!")



        error = self.result[1]
        self.task = self.result[0]

        if error:
            Messagebox.show_info(title="Info", message=error)

        else:
            for item in self.task_item:
                self.table.delete(item)
            self.task_item.clear()

            row = 1
            for item in self.task:
                item = self.table.insert("", END,
                                         text=str(row),
                                         iid=item.task_id,
                                         values=(item.name,
                                                item.detail,
                                                 item.date_task,
                                                 item.finish_date,
                                                 "Done" if item.condition == 1 else "In Progress",
                                                 f"{item.complete}%"

                                                 ))
                self.task_item.append(item)
                row += 1

            self.table.column("#0" , width=200 , anchor="center")

            for i in self.column:
                self.table.column(i , width=300 , anchor="center")

    def add_button_clicked(self):
        self.view.switch("add")

        add_task = self.view.switch("add")
        add_task.get_id(self.current_id)

    def show_task(self):
        for task_id in self.table.selection():
            task = self.business.get_task(task_id)
            show_task = self.view.switch("show")
            show_task.get_current_task(task)
            show_task.get_user(self.current_id)

    def back_clicked(self):
        self.view.switch("login")
        self.reset_combobox()
        self.reset_combobox_sort()
        self.load_data_task()

    def delete(self):
        for id in self.table.selection():
            self.business.delete_task(id)

        self.load_data_task()

    def done_clicked(self):

        for id in self.table.selection():
            self.business.done_task(id , 1 , 100)
        self.load_data_task()


    def sort_persent(self):
        percents =[]
        tasks = []
        data = self.combobox_sort.get()
        if data == "Most Complete Percent":
            for item in self.task:
                percents.append(int(item.complete))
                self.current_user_id = item.user_id
            sort_complete = sorted(percents , reverse=True)


            for item_t in sort_complete:
                result = self.business.sort_complete_business(item_t , self.current_user_id)
                task = result[0]
                for i in task:
                    tasks.append(i)
            return (tasks , None)

    def sort_title(self):
        names =[]
        tasks = []
        data = self.combobox_sort.get()
        if data == "Title":
            for item in self.task:
                names.append(item.name)
                self.current_user_id = item.user_id
            sort_name = sorted(names)
            for item_t in sort_name:
                result = self.business.sort_title_business(item_t , self.current_user_id)
                task = result[0]
                for i in task:
                    tasks.append(i)
            return (tasks , None)












