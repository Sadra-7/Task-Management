import datetime
import sqlite3
from Task_management.Common_layer.user import User , Task , Make_Task

class User_data:
    date_now = datetime.datetime.now()
    def __init__(self):
        self.data_base = "Task.db"


    def check_user(self , username , password):

        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT id,
            firstname,
       username,
       password
  FROM User Where
  username = ? AND password = ?
""" , [username , password]).fetchone()

            if data:

                user = User.user_make(data)
                return user
            else:
                return None

    def load_task_data(self,user_id):
        tasks_item = []
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT *
  FROM Tasks Where user_id = ?
""" , [user_id]).fetchall()

        if data:

            for item in data:
                task = Task(item[0] , item[1],item[2],item[3],item[4],item[5],item[6],item[7])
                tasks_item.append(task)

            return tasks_item

        else:
            return None

    def add_user(self , firstname , username , password):
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO User(
            
            username,
            password,
            firstname) VALUES (
            
            '{username}',
            '{password}',
            '{firstname}');""").fetchall()

    def add_task(self,name , detail , date , user_id):
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO Tasks(
                user_id,
                name,
                detail,
                date_task,
                finish_date) VALUES (
                '{user_id}',
                '{name}' , 
                '{detail}' , 
                '{f"{self.date_now.year}-{self.date_now.month}-{self.date_now.day}"}',
                '{date}');""").fetchall()


    def show_task_data(self,task_id):
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT * FROM Tasks WHERE task_id = ?""" , [task_id]).fetchone()

            if data:
                task = Make_Task.make_task(data)
                return task

    def edit_task_data(self , task_id , name , detail , date , complete):

        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""UPDATE Tasks
   SET 
       name = '{name}',
       detail = '{detail}',
       finish_date = '{date}',
       complete = '{complete}'
 WHERE 
task_id = ?
""" , [task_id])
            connection.commit()


    def delete_task_data(self , task_id):
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM Tasks
      WHERE 
    task_id = ?
""" , [task_id])
            connection.commit()

    def change_condition_data(self,id,condition , complete):
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""UPDATE Tasks
   SET 
    codition = '{condition}',
    complete = '{complete}'

 WHERE 
       task_id = ?
""" , [id])
            connection.commit()

    def search_data(self , codition , id):
        tasks_item = []
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
    SELECT user_id,
       name,
       detail,
       date_task,
       codition,
       complete,
       task_id,
       finish_date
  FROM Tasks Where codition = ? AND user_id = ?
""" , [codition , id]).fetchall()



            if data:

                for item in data:
                    task = Task(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                    tasks_item.append(task)


                return tasks_item
            else:
                return None

    def sort_data_title(self , title , id):
        sort_tasks_item = []
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT user_id,
       name,
       detail,
       date_task,
       codition,
       complete,
       task_id,
       finish_date
  FROM Tasks WHERE user_id = ? AND name = ?
""" , [id , title]).fetchall()

            if data:
                for item in data:
                    task = Task(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                    sort_tasks_item.append(task)

                return sort_tasks_item
            else:
                return None

    def sort_data_complete(self, complete , id):
        sort_tasks_item = []
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT user_id,
           name,
           detail,
           date_task,
           codition,
           complete,
           task_id,
           finish_date
      FROM Tasks WHERE user_id = ? AND complete = ?
    """, [id , complete]).fetchall()

            if data:
                for item in data:
                    task = Task(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                    sort_tasks_item.append(task)

                return sort_tasks_item
            else:
                return None








