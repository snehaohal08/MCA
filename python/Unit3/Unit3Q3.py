#13. Operator Overloading
#Write a program to overload the + operator to add two complex numbers using a Complex class.


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(2, 3)
c2 = Complex(5, 7)

print(c1 + c2)
    