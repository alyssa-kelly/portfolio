class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        string = 'Rectangle(width={0}, height={1})'.format(self.width, self.height)
        return string
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self): 
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    
    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*".
        The number of lines should be equal to the height and the number
        of "*" in each line should be equal to the width. There should
        be a new line (\n) at the end of each line. If the width or
        height is larger than 50, this should return the string:
        "Too big for picture.".
        """
        if (self.width > 50) or (self.height > 50):
            line = "Too big for picture."
        else:
            line = ''
            for i in range(self.height):
                line += ("*" * self.width) + '\n'
        return line 
        
    def get_amount_inside(self, shape):
        """
        Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit
        inside the shape (with no rotations). For instance, a rectangle
        with a width of 4 and a height of 8 could fit in two squares
        with sides of 4.
        """
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def __str__(self):
        string = 'Square(side={0})'.format(self.width)
        return string
    
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)