


class Mobile():

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


xiomi = Mobile("Xiomi", "Redmi 13 pro")
xiomi.display()

sm = Mobile("Samsung", "Galaxy")
sm.display()



