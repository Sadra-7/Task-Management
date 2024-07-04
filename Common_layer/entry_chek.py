from ttkbootstrap.dialogs import Messagebox

class EntryDescriptor:

    def __init__(self , min , object_name:str):
        self.min = min
        self.object_name = object_name

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attr]

    def __set__(self, instance, value):
        self.value = value
        if not isinstance(value , str) or len(value)<self.min:
            Messagebox.show_error(title="ERROR!" , message=f"{self.object_name} need {self.min} character")
            raise ValueError
        else:
            instance.__dict__[self._attr] = value
