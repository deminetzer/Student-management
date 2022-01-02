from course import Course


class Student:
    """
        A class to represent a student

        Attributes
        ----------
        name : (str) name of student
        _id : (str) student's ID number
        courses: (list) list of student's courses
    """

    def __init__(self, name, id):
        """
             The constructor for student class. Empty List of courses for new student.

             Parameters:
                name (str): The name of the student.
                id (str): student's ID number
         """
        self.name = name
        self._id = id
        self.courses = []

    def getID(self):
        """ Function returns student's ID number """
        return self._id

    def addCourse(self, newCourse):
        """
            Function to add a new course to the list of courses.
            Only courses with valid grade will be added.

            Parameters:
                newCourse (Course): New course to add

            Returns: True - if the grade of the course is valid and the course added to the list, False - otherwise.
        """
        if int(newCourse.grade) < 0 or int(newCourse.grade) > 100:
            return False
        self.courses.append(newCourse)
        return True

    def courseExist(self, course):
        """
            Function to check if a course exist in the list of courses.

            Parameters:
                course (Course): course to check if exist in the list of courses

            Returns: True - if the course exist in the list, False - otherwise.
        """
        for c in self.courses:
            if c.c_name == course.c_name:
                return True
        return False

    def __str__(self):
        """ Function to represent student as a string"""
        courses_str = "[ "
        courses_str = courses_str + ", ".join(str(x) for x in self.courses)
        courses_str = courses_str + " ]"
        return f'{self.name}, {self._id}, {courses_str}'

