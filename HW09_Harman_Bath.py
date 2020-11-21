"""
All the students info is stored in a dictionary, where the key is CWID, the value is an instance is Student.
All the instructors info is stored in a dictionary, where the key is CWID, the value is an instance is Instructor.
All the majors info is stored in dictionary, where the key is major name, the value is an instance of Major
"""

import os
from student import Student
from instructor import Instructor
from prettytable import PrettyTable
from major import Major
from HW08_Harman_Bath import file_reader
import sqlite3

DB_PATH = 'C:\\Users\\hrmnv\\Desktop\\SSW_810\\Student-Repository\\HW_11\\mydb.db'

class University:
    """
    Store all info for all students and instructors
    """

    def __init__(self, path):
        """
        Specify directory path where the files are to be accessed
        """
        self.students_path = os.path.join(path, 'students.txt')
        self.instructors_path = os.path.join(path, 'instructors.txt')
        self.grades_path = os.path.join(path, 'grades.txt')
        self.majors_path = os.path.join(path, 'majors.txt')


        self.students = dict() 
        self.instructors = dict() 
        self.majors = dict() 

        self.majors_DB()
        self.students_DB()
        self.instructors_DB()
        self.grades_DB()
        
        self.print_major_table()
        self.print_student_table()
        self.print_instructor_table()
        self.student_grades_table_db(DB_PATH)

        

    def students_DB(self):
        """
        CWID, Name, Major
        """

        for student in file_reader(self.students_path, 3, sep = '\t', header=True):
            CWID, name, major = student

            if major not in self.majors:
                raise ValueError('Missing major {} !'.format(major))

            if CWID not in self.students:
                self.students[CWID] = Student(student, self.majors[major])

    def instructors_DB(self):
        """
        CWID, Name, Department
        """

        for instructor in file_reader(self.instructors_path, 3, sep = '\t', header=True):
            self.instructors[instructor[0]] = Instructor(instructor)


    def grades_DB(self):
        """ 
        Structure: CWID_student, Course, Grade, CWID_instructor
        """

        for CWID_student, course, grade, CWID_instructor in file_reader(self.grades_path, 4, sep = '\t', header=True):
            if CWID_student not in self.students.keys():
                raise ValueError('Student CWID {} is not in the student system.'.format(CWID_student))
            
            if CWID_instructor not in self.instructors.keys():
                raise ValueError('Instructor CWID {} is not in the instructor system.'.format(CWID_instructor))
            
            self.students[CWID_student].add_course(course, grade) 
            self.instructors[CWID_instructor].add_course(course)



    def majors_DB(self):
        """ 
        Structure: Department, Flag, Course
        """

        for major, flag, course in file_reader(self.majors_path, 3, sep = '\t', header=True):
            if major not in self.majors:
                self.majors[major] = Major(major)

            self.majors[major].update_major(flag, course)

    def print_student_table(self):
        """ 
        generate the prettytable for students summary
        """
        
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA'])
        for student in self.students.values():
            # calculating remaining required and elective courses
            courses = self.majors[student.major].update_courses(student.courses)

            CWID, name, major, c = student.student_info()
            student_info = [CWID, name, major] #ignore the courses info
            for item in courses:
                student_info.append(item)

            pt.add_row(student_info)
        print('Students Summary')
        print(pt)
        
    def print_instructor_table(self):
        """
        generate the prettytable for instructors summary
        """

        pt = PrettyTable(field_names = ['CWID', 'Name', 'Department', 'Courses', 'No. of Students'])
        for instructor in self.instructors.values():
            for item in instructor.instructor_info():
                pt.add_row(item)
        print('Instructors Summary')
        print(pt)

    def print_major_table(self):
        """
        generate the prettytable for majors summary
        """

        pt = PrettyTable(field_names = ['Major', 'Required Courses', 'Electives'])
        for major in self.majors.values():
            pt.add_row(major.major_info())

        print('Majors Summary')
        print(pt)

    def student_grades_table_db(self, DB_PATH):
        db = sqlite3.connect(DB_PATH)

        query = """SELECT s.Name, s.CWID, g.Course, g.Grade, i.Name
                   FROM students s, grades g, instructors i 
                   WHERE g.InstructorCWID = i.CWID
                   AND  s.CWID = g.StudentCWID ORDER BY s.Name;"""

        pt = PrettyTable(field_names = ['Name','CWID','Course','Grade','Instructor'])

        for row in db.execute(query):
            pt.add_row(row)

        print(pt)
        


def main():
    path = 'C:\\Users\\hrmnv\\Desktop\\SSW_810\\Student-Repository\\HW_11'
    University(path)

if __name__ == '__main__':
    main()