class Rectangle:

  def __init__(self, width, height):
    self.width = width  
    self.height = height

    def set_width(self):
      return(self.width)

    def set_height(self):
      return(self.height)

    def get_area(self):
      return(self.width * self.height)

    def get_perimeter(self):
      return((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
      return(((self.width ** 2) + (self.height ** 2)) ** .5)

    def get_picture(self):
      pass

    def get_amount_inside(self):
      pass
      


class Square(Rectangle):

    def set_side(self, side):
      self.width = side
      self.height = side