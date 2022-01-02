class Course:
    """
        A class to represent a course

        Attributes
        ----------
        c_name : (str) name of the course
        grade : (str) grade of the course
    """

    def __init__(self, c_name):
        """
            The constructor for course class. The grade of a new course is 101.

            Parameters:
                c_name (str): The name of the course.
        """
        self.c_name = c_name
        self.grade = 101

    def setGrade(self, grade):
        """
            The function to set the grade of the course, only if the grade is valid

            Parameters:
                grade: (str) The new grade

            Returns: True - if the grade is valid and determined to be the course grade, False - otherwise.
        """
        if int(grade) < 0 or int(grade) > 100:
            return False
        else:
            self.grade = grade
            return True

    def __str__(self):
        """ Function to represent course as a string"""
        return f'{self.c_name} {self.grade}'

