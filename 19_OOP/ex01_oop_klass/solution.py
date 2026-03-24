"""Simple class."""

class Teacher:

    def __init__(self):
        super().__init__()
        self.school = "Tallinna Tööstushariduskeskus"
        self.group = []
        self.subjects = []


class Student:
    """Student class."""

    def __init__(self, name = "Anonymous", finished=False):
        """Construct a Student instance."""
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student_1 = Student()
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False