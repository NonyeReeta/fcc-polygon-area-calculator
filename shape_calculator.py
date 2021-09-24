class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, n):
        self.width = n
        return self.width

    def set_height(self, n):
        self.height = n
        return self.height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for m in range(self.height):
                for n in range(self.width):
                    picture += "*"
                picture += "\n"
            return picture

    def get_amount_inside(self, shape):
        return self.width // shape.width



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, n):
        self.width = n
        self.height = n
        self.side = n
        return self.width, self.height, self.side






