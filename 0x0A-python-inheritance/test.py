#!/usr/bin/python3



class Base():
    """
    """
    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    def __init__(self):
        super().__init__()
        self.id += 99
u = User()
print(u.id)
