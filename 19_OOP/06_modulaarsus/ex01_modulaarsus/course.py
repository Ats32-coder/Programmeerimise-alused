"""Course module for school system."""


class Course:
    """Represent a course and store student grades."""

    def __init__(self, name: str):
        """Initialize a course.

        Args:
            name (str): Course name.
        """
        self.name = name
        self.grades = []

    def add_grade(self, student, grade: int):
        """Add a grade for a student.

        Args:
            student: Student object.
            grade (int): Grade value.
        """
        self.grades.append((student, grade))

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