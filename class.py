class BIRD:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def fly(self):
        print("I can fly")
        print("my color is", self.color)
        print("my weight is", self.weight)

class Peacock(BIRD):
    def __init__(self, color, weight, flying_height):
        BIRD.__init__(self, color, weight)
        self.flying_height = flying_height

    def print_flying_height(self):
        print(f"I can fly up to {self.flying_height} feet high")

class Eagle(BIRD):
    def __init__(self, color, weight, flying_height):
        BIRD.__init__(self, color, weight)
        self.flying_height = flying_height

    def print_flying_height(self):
        print(f"I can fly up to {self.flying_height} feet high")

peacock = Peacock("Blue", 10, 20)
eagle = Eagle("Brown", 15, 30)

peacock.print_flying_height()
peacock
eagle.print_flying_height()
