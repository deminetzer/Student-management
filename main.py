from course import Course
from student import Student
import sys


temp_students = []
students = []
temp_courses = []
courses = []


"""Get a filename that contains students details"""
f_name = input("Enter a file name : ")
try:
    with open(f'{f_name}.txt', 'r') as f:
        for line in f:
            temp_students.append(line.rstrip())
except OSError as err:
    print(f"OS error: {err}.")
    sys.exit(1)  # if the file is not exist - exit


"""Create a student list"""
for s in temp_students:
    s = s.split("\t")
    student = Student(s[0], s[1])
    if len(s) == 3:  # If the student has courses
        temp_courses = s[2].split(";")
        for c in temp_courses:
            c = c.split("#")
            course = Course(c[0])
            course.setGrade(c[1])
            if not(student.courseExist(course)):
                student.addCourse(course)
                courses.append(course)
    students.append(student)


def average(courses):
    """
    Function to calculate average of grades.

    Parameters:
        courses (List): List of courses

    Returns: if there is at least one course in "courses" - the function returns the average of all the grades.
            else, the function returns -1.
    """
    if len(courses) > 0:
        return sum(courses)/len(courses)
    return -1


def id_and_avg(stud):
    """
    Function creates a string of student's ID number and average

    Parameters:
        stud (Student): student

    Returns: A string contains student's ID number and average
    """
    return f'{stud.getID()} {average(list(map(lambda c: int(c.grade), stud.courses)))}'


select = 0
while select != "4":  # 4 = exit

    select = input("Menu : \n1. Calculating the average of a particular student\n"
                   "2. Calculating the average of a particular course\n"
                   "3. Calculation of the average of all students\n"
                   "4. Exit\n")

    if select == "1":  # Calculate the average of particular student
        name = input("Enter name of student: ")
        avg = " ".join(map(id_and_avg, (filter(lambda s: s.name == name, students))))
        if len(avg) == 0:
            print("Student not found")
        else:
            print(avg)

    elif select == "2":  # Calculate the average of particular course
        name = input("Enter name of course: ")
        avg = average(list(map((lambda c3: int(c3.grade)), filter((lambda c4, n=name: n == c4.c_name), courses))))
        if avg == -1:
            print("Course not found")
        else:
            print(name, avg)

    elif select == "3":  # Write in a file all the IDs of all the students and all their averages
        f_name = input("Enter a file name : ")
        with open(f'{f_name}.txt', 'w') as f:
            f.write("\n".join(list(map(id_and_avg, students))))
            print("Done !\n")

    elif select != "4":
        print("Invalid input ! Enter number between 1-4\n")


print("Goodbye")
