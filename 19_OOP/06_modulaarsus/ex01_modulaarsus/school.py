"""School module that manages students and courses."""

from student import Student
from course import Course


class School:
    """Represent a school that manages students, courses and grades."""

    def __init__(self, name: str):
        """Initialize a school.

        Args:
            name (str): School name.
        """
        self.name = name
        self.students = []
        self.courses = []
        self._next_id = 1

    def add_student(self, student: Student):
        """Add a student to the school.

        Assigns a unique ID if student is new.
        """
        if student not in self.students:
            self.students.append(student)
            student.set_id(self._next_id)
            self._next_id += 1

    def add_course(self, course: Course):
        """Add a course to the school."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add a grade for a student in a course."""
        if student not in self.students:
            return
        if course not in self.courses:
            return

        student.add_grade(course, grade)
        course.add_grade(student, grade)

    def get_students(self):
        """Return all students."""
        return self.students

    def get_courses(self):
        """Return all courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self):
        """Return students sorted by average grade (descending)."""
        return sorted(
            self.students,
            key=lambda student: student.get_average_grade(),
            reverse=True
        )