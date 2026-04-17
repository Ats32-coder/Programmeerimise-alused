"""Student module for school system."""


class Student:
    """Represent a student and store their grades."""

    def __init__(self, name: str):
        """Initialize a student.

        Args:
            name (str): Student name.
        """
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        """Set student ID once.

        Args:
            id (int): Unique identifier.
        """
        if self.id is None:
            self.id = id

    def get_id(self):
        """Return student ID."""
        return self.id

    def add_grade(self, course, grade: int):
        """Add a grade for a course.

        Args:
            course: Course object.
            grade (int): Grade value.
        """
        self.grades.append((course, grade))

    def get_grades(self):
        """Return all grades."""
        return self.grades

    def get_average_grade(self):
        """Return average grade or -1 if none."""
        if not self.grades:
            return -1
        return sum(g for _, g in self.grades) / len(self.grades)

    def __repr__(self):
        """Return string representation."""
        return self.name