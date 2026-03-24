"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Initialize Person object."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Initialize Student object."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty_object = Empty()

    # 3 x person usage
    p1 = Person()
    p1.firstname = "Tiit"
    p1.lastname = "Sukk"
    p1.age = 40
    p2 = Person()
    p2.firstname = "Teet"
    p2.lastname = "Pall"
    p2.age = 30
    p3 = Person()
    p3.firstname = "Mart"
    p3.lastname = "Lembit"
    p3.age = 68

    # 3 x student usage
    s = Student("Albert", "Kukk", 22)
    s1 = Student("Meelis", "Mesi", 40)
    s2 = Student("Toomas", "Mänd", 9)
