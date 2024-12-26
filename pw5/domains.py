class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.credits = 0
        self.marks = []

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, course_name, credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}, Credits: {self.credit}"