class Vactor_2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2DVactor is {self.i}i + {self.j}j")


class Vactor_3D(Vactor_2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The 2DVactor is {self.i}i+ {self.j}j+ {self.k}k")

c = Vactor_2D(1,2)
d = Vactor_3D(1,2,3)
d.show()
c.show()