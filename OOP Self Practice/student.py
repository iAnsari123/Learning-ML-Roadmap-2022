class Student:
    __number_of_students = 0
    __school_name = "Maple Leaf International School"

    def __init__(self, name: str, age: int, gender: str, marks: int) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks
        self.school_name = Student.__school_name
        Student.__number_of_students += 1

    def __str__(self) -> str:
        return f"{'His' if self.gender == 'male' else 'Her'} name is {self.name}, {self.age} years old, studies in {self.school_name}, and got {self.marks}"

    @classmethod
    def get_total_students(cls):
        return f"Total number of students are: {cls.__number_of_students}"

    @classmethod
    def set_total_students(cls, security_code: int, total_student: int = 0):
        if security_code == cls.__password():
            Student.__number_of_students = total_student
            return f"Total number of students changed to {Student.__number_of_students}"
        else:
            return "Please enter correct security code"

    @staticmethod
    def __password():
        return 0


nokib = Student("Nakib", 23, "male", 90)
sinthia = Student("Sinthia", 23, "female", 80)
print(nokib)
print(sinthia)
print(Student.get_total_students())
print(Student.set_total_students(0))
print(nokib.get_total_students())
