class User:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def login(self):
        return "Successfully logged in"

    def __logout(self):
        return "Successfully logged out"

    def parent(self):
        return f"I'm inside parent"


class Student(User):

    def parent(self):
        print(super().parent())
        return f"I'm inside child"

    # def __init__(self, name, id) -> None:
    #     super().__init__(name, id)
    #     print("successfully created a student")


nokib = Student(1,2)
print(nokib.login())
print(nokib.parent())
# print(nokib.logout())
