import re


class Student:

    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")

    def grades_tuple(self):
        return tuple(self.grades)

    def has_valid_email(self):
        email_pattern = r"^[A-Za-z]+@[A-Za-z]+\.(com)$"
        return re.match(email_pattern, self.email) is not None


def get_student_by_email(email):
    return student_dict.get(email)


student1 = Student("Ava", "ava@codingtemple.com", [92, 53, 12])
student2 = Student("Mateo", "mateo@codingtemple.com", [98, 90, 94])
student3 = Student("Nia", "nia@codingtemple.com", [76, 89, 95])

students = [student1, student2, student3]


student1.add_grade(96)
student1.add_grade(84)

student2.add_grade(90)
student2.add_grade(98)

student3.add_grade(87)
student3.add_grade(93)


student_dict = {
    student.email: student
    for student in students
}


print("STUDENT INFORMATION")
print("-------------------")
for student in students:
    student.display_info()
    print(f"Valid Email: {student.has_valid_email()}")
    print()


email_to_find = "mateo@codingtempl.com"
found_student = get_student_by_email(email_to_find)
if found_student:
    print(f"Found student for {email_to_find}: {found_student.name}")
else:
    print(f"No student found for {email_to_find}.")

missing_email = "nia@codingtemple.com"
missing_student = get_student_by_email(missing_email)
if missing_student:
    print(f"Found student for {missing_email}: {missing_student.name}")
else:
    print(f"No student found for {missing_email}.")

print()


unique_grades = set()
for student in students:
    unique_grades.update(student.grades)

print(f"Unique grades across all students: {unique_grades}")
print()

print("TUPLE IMMUTABILITY DEMONSTRATION")
print("--------------------------------")
for student in students:
    grade_tuple = student.grades_tuple()
    print(f"{student.name}'s grades as a tuple: {grade_tuple}")

    try:
        grade_tuple[0] = 100
    except TypeError:
        print("Tuples are immutable, so their values cannot be changed.")

print()

print("LIST OPERATIONS AFTER POP")
print("-------------------------")
for student in students:
    removed_grade = student.grades.pop()
    print(f"{student.name}'s removed grade: {removed_grade}")
    print(f"First grade: {student.grades[0]}")
    print(f"Last grade: {student.grades[-1]}")
    print(f"Number of grades: {len(student.grades)}")
    print()

grades_above_90 = 0
for student in students:
    for grade in student.grades:
        if grade > 90:
            grades_above_90 += 1

print(f"Number of grades above 90 after pop operations: {grades_above_90}")