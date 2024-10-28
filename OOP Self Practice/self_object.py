# create a class
class Fraction:
    object_created = 0

    def __init__(self, x: int, y: int) -> None:
        self.numerator: int = x
        self.denomitor: int = y
        Fraction.object_created = Fraction.object_created + 1

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denomitor}"

    def __add__(self, num):
        temp_numerator = self.numerator * num.denomitor + num.numerator * self.denomitor
        temp_denomitor = self.denomitor * num.denomitor

        return Fraction(temp_numerator, temp_denomitor)

    def __sub__(self, num):
        temp_numerator = self.numerator * num.denomitor - num.numerator * self.denomitor
        temp_denomitor = self.denomitor * num.denomitor

        return Fraction(temp_numerator, temp_denomitor)

    def __mul__(self, num):
        temp_numerator = self.numerator * num.numerator
        temp_denomitor = self.denomitor * num.denomitor

        return Fraction(temp_numerator, temp_denomitor)

    def created_object(self):
        print(f"So far {Fraction.object_created} objects has been created")


# create object of Room class
fr1 = Fraction(2, 3)
fr2 = Fraction(3, 4)


# print(fr1 * fr2)
fr2.created_object()
fr1.created_object()
