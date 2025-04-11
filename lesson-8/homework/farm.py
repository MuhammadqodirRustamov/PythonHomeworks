class Animal:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def walk(self):
        print("Walk")

    def run(self):
        print("Run")

    def sleep(self):
        print("Sleep")

    def make_sound(self):
        print("Make sound")

    def eat(self):
        print("Eat")


class Cow(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def make_sound(self):
        print("Mooo")

    def eat(self):
        print("Eat grass")


class Chicken(Animal):
    def __init__(self, name, gender):
        super().__init__(name, True)

    def make_sound(self):
        print("Cock a doodle doo")

    def eat(self):
        print("Eat everything organic")

    def fly(self):
        print("Kind of fly")


class Rooster(Chicken):
    def __init__(self, name):
        super().__init__(name, True)


class Hen(Chicken):
    def __init__(self, name):
        super().__init__(name, False)

    def lay_eggs(self):
        print("Lay eggs")


class Horse(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def make_sound(self):
        print("Neigh")

    def eat(self):
        print("Eat grass")
