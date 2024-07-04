

class UserDescriptor:

    def __init__(self , min):
        self.min = min

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attr]

    def __set__(self, instance, value):

        if not isinstance(value , str) or len(value)<self.min :
            raise ValueError(f"Invalid username or password")
        instance.__dict__[self._attr] = value
