from ttkbootstrap import *

class Window_task(Window):
    def __init__(self, weight=1000, height=590):
        super().__init__(themename="cyborg" , title="Task Manager")

        self.grid_rowconfigure(0 , weight=1)
        self.grid_columnconfigure(0 , weight=1)

        self.geometry(f"{weight}x{height}")

    def show(self):
        self.mainloop()


