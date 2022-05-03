#class inhertance
#say you may a chef class and a pastry chef class, you want the pastry chef class to inherit vars and functions from the chef class


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swim, Swam")
    
    def breathe(self):
        print("Underwater breathe")
        super().breathe()



nemo = Fish()
stangus = Animal()

nemo.swim()
nemo.breathe()

stangus.breathe()
print(nemo.num_eyes)