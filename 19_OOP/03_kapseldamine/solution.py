"""Exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, student_id: int):
        """Initialize student object."""
        self.__name = name
        self.__id = student_id
        self.__status = "Active"

    def get_id(self):
        """Return student id."""
        return self.__id

    def set_name(self, name: str):
        """Set the name of the student."""
        self.__name = name

    def get_name(self):
        """Return student name."""
        return self.__name

    def set_status(self, status):
        """Set the status of the student only if given status in correct."""
        allowed_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        if status in allowed_statuses:
            self.__status = status

    def get_status(self):
        """Return student status."""
        return self.__status