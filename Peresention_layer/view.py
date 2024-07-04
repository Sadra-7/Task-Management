from .window import Window_task
from .start import Welcome
from .login_frame import Login_fram
from .home import Home
from .add import Add
from .new_account import Create
from .show_info import Show
from .edit import Edit


class View:
    def __init__(self):
        self.window = Window_task()

        self.frames = {}


        self.frame("edit" , Edit(self, self.window))
        self.frame("show" , Show(self , self.window))
        self.frame("add" , Add(self , self.window))
        self.frame("home" , Home(self , self.window))
        self.frame("login" , Login_fram(self , self.window))
        self.frame("create" , Create(self , self.window))
        self.frame("welcome" , Welcome(self , self.window))


        self.window.show()

    def frame(self, name , frame):
        self.frames[name] = frame
        self.frames[name].grid(row = 0 , column = 0 , sticky = "nsew")

    def switch(self , frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]


