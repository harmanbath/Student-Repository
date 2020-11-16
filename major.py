  
"""
Implementing Major class that stores all information about a major
'R' --> required course
'E' --> elective course
"""
class Major:
    """
    Major, Required course, Electives
    """
    def __init__(self, major):
        """ 
        major, required courses, elective courses
        """

        self.major = major

        self.required = set()
        self.elective = set()

    def update_major(self, flag, course):
        """ 
        update the required courses('R') and the electives('E') 
        """
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.elective.add(course)
        else:
            raise ValueError("Unknown course flag")

    def update_courses(self, courses):
        """ calculate the successfully completed courses, remaining required, elective courses"""
        passing_grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C') 
        GPA_scale ={'A' : 4.0, 'A-': 3.75,'B+': 3.25,'B' : 3.0,'B-': 2.75,'C+': 2.25,'C' : 2.0,}
        GPA = 0
        completed_courses = set()
        for course, grade in courses.items():
            if grade == ' ': 
                continue
            elif grade in passing_grades:
                GPA += GPA_scale[grade]
                completed_courses.add(course)
        
        if len(completed_courses) == 0:
            GPA = 0.0
        else:
            GPA /= len(completed_courses)
        
        remaining_required = self.required_courses(completed_courses)
        remaining_electives = self.elective_courses(completed_courses)

        return [sorted(list(completed_courses)), remaining_required, remaining_electives, round(GPA,2)]

    def required_courses(self, courses):
        """ 
        return remaining required courses 
        """
        if self.required.difference(courses) == set():
            return None
        else:
            return sorted(list(self.required.difference(courses)))

    def elective_courses(self, courses):
        """ 
        return remaining electives 
        """
        left_courses = self.elective.difference(courses)
        if len(left_courses) < len(self.elective): 
            return None
        else:
            return sorted(list(self.elective))

    def major_info(self):
        """ 
        return the info for prettytable
        """
        return [self.major, sorted(list(self.required)), sorted(list(self.elective))]

