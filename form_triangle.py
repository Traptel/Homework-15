class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TriangleChecker(Triangle):
    def is_triangle(self):
        if not (isinstance(self.a, (int, float))
                and isinstance(self.b, (int, float))
                and isinstance(self.c, (int, float))):
            return "- Потрібно вводити тільки числа!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "- З негативними числами нічого не вийде!"
        elif (self.a + self.b > self.c
              and self.a + self.c > self.b
              and self.b + self.c > self.a):
            return "- Ура, можна побудувати трикутник!"
        else:
            return "- Жаль, але з цього трикутник не зробити."


class ExtTriangle(TriangleChecker, Triangle):
    pass


triangle_1 = ExtTriangle(3.5, 4, 5)
print(triangle_1.is_triangle(),)

triangle_2 = ExtTriangle(-5, -1, 9)
print(triangle_2.is_triangle(),)

triangle_3 = ExtTriangle("3", 4, 5)
print(triangle_3.is_triangle(),)

triangle_4 = ExtTriangle(4, 4, 9)
print(triangle_4.is_triangle(),)
