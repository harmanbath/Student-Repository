"""
Implementing the Students class for storing the information for a single student
Student : CWID, Name, Major, Courses
"""

from collections import defaultdict
from major import Major
class Student:
    """
    Stores the info for a single student with the following information:
    CWID, name, major, courses with grades
    """

    def __init__(self, student_info, major_info):
        """
        CWID: str
        name : str
        major : str
        courses : defaultdict(str)
        """
        if len(student_info) == 2 or any([item.isspace() for item in student_info]) or '' in student_info:
            raise ValueError("Missing student information")
        self.CWID, self.name, self.major = student_info
        self.major_info = major_info
        self.courses = defaultdict(str)

    def add_course (self, course, grade):
        """
        Key: course, Value: grade
        """
        self.courses[course] = grade

    def student_info(self):
        """ 
        return the details for a single student in a list 
        """
        if not self.courses.items():
            return [self.CWID, self.name, self.major, None, None]
        else:
            return [self.CWID, self.name, self.major, sorted(list(self.courses.keys()))]
