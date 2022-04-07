class Rectangle:

    def __init__(self, width, height):
        self.width = width  
        self.height = height
        #print("================== __init__")
        #print(self.width, self.height)

    def set_width(self, width):
        #print("================== set_width")
        #print(width)
        self.width = width
        return(self.width)

    def set_height(self, height):
        #print("================== set_height")
        #print(height)
        self.height = height
        return(self.height)

    def get_area(self):
        #print("================== get_area")
        #print(self.width * self.height)
        return(self.width * self.height)

    def get_perimeter(self):
        #print("================== get_perimeter")
        #print((2 * self.width) + (2 * self.height))
        return((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        #print("================== get_diagonal")
        #print(((self.width ** 2) + (self.height ** 2)) ** .5)
        return(((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
        #print("================== get_picture")
        #print(self)

        if self.width > 50 or self.height > 50:
            return (f"Too big for picture.")

        s_shape = ""
        for row in range(0, self.height):
            for col in range(0, self.width): 
                s_shape += "*"
            s_shape += "\n"
        return(s_shape)
        
    

    def get_amount_inside(self, shape):
      print(f"==============get_amount_inside shape= {shape}")
      print(f"==============get_amount_inside self= {self}")
      
    def __repr__(self):
        return(f"Rectangle(width={self.width}, height={self.height})")

class Square(Rectangle):

    def __init__(self, side):
        self.width = side  
        self.height = side
        self.side = side

    def set_side(self, side):
        self.side = side
        self.width = side  
        self.height = side


    def __repr__(self):
        return(f"Square(side={self.side})")