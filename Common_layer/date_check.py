from datetime import date
from ttkbootstrap.dialogs import Messagebox

class Date:

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attr]

    def __set__(self, instance, value):

        try:
            current_date = date.fromisoformat(value)
            if not isinstance(current_date , date):
                Messagebox.show_error(title="ERROR!", message=f"Invalid date (0000-00-00)")
            else:
                instance.__dict__[self._attr] = value
        except:
            Messagebox.show_error(title="ERROR!", message=f"Invalid date\ndate format : (0000-00-00)")
