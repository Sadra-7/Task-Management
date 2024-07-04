from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    id : int
    firstname : str
    username : str
    password : None or str

    @classmethod
    def user_make(cls , data:tuple):
        return cls(data[0] , data[1] , data[2] , None)


@dataclass
class Make_Task:
    user_id : int
    name: str
    detail: str
    date_task: date
    condition: str
    complete: int
    task_id : int
    finish_date : date

    @classmethod
    def make_task(cls , data : tuple):
        return cls(data[0] , data[1] , data[2] , data[3],data[4] , data[5] , data[6] , data[7])

class Task:
    def __init__(self , user_id ,name,detail,date_task,condition,complete,task_id,finish_date):

        self.user_id = user_id
        self.name = name
        self.detail = detail
        self.finish_date = finish_date
        self.date_task = date_task
        self.condition = condition
        self.complete = complete
        self.task_id = task_id






