"""
Implementing the Instructors class for storing the information for a single Instructor
Instructor : CWID, Name, Department, Courses, Number of students
"""

from collections import defaultdict

class Instructor:
    """
    Stores information about a single Instructor with the following information information:
    CWID, name, department, courses with No. of students
    """

    def __init__(self, instructor_info):
        """
        CWID: str
        name: str
        department: str
        courses: defaultdict(int)
        """
        self.CWID, self.name, self.department = instructor_info
        self.courses = defaultdict(int)

    def add_course(self, course):
        """
        key: course, value : no. of students
        """
        self.courses[course] += 1

    def instructor_info(self):
        """
        return details for single instructor
        """
        info = list()

        if not self.courses.items(): # If no courses
            info.append([self.CWID, self.name, self.department, None, None]) 
        else:
            for course, students in self.courses.items():
                info.append([self.CWID, self.name, self.department, course, students])
        return info




