class Rectangle:

    def __init__(self, width, height):
        self.width = width  
        self.height = height
        
    def set_width(self, width):
        self.width = width
        return(self.width)

    def set_height(self, height):
        self.height = height
        return(self.height)

    def get_area(self):
        return(self.width * self.height)

    def get_perimeter(self):
        return((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return(((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return (f"Too big for picture.")

        #s_shape = ""
        #for row in range(0, self.height):
        #    for col in range(0, self.width): 
        #        s_shape += "*"
        #    s_shape += "\n"
        #
        # or only one line (("*" * self.width) + "\n") * self.height

        s_shape = (("*" * self.width) + "\n") * self.height
        return(s_shape)
        
    def get_amount_inside(self, shape):
      return(int(self.get_area() / shape.get_area()))
      
    def __str__(self):
        return(f"Rectangle(width={self.width}, height={self.height})")

class Square(Rectangle):

    def __init__(self, side):
        self.width = side  
        self.height = side

    def set_side(self, side):
        self.width = side  
        self.height = side

    def set_width(self, side):
        self.width = side  
        self.height = side

    def set_height(self, side):
        self.width = side  
        self.height = side
    
    def __str__(self):
        return(f"Square(side={self.width})")