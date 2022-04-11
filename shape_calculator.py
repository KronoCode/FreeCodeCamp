class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    

  def set_width(self,change_width):
    self.width=change_width

  def set_height(self,change_height):
    self.height=change_height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return (self.width+self.height)*2

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture=''
    if self.height>50 or self.width>50:
      return 'Too big for picture.'
    else:
      for _ in range(self.height):
        picture+='*'*self.width+'\n'
      return picture

  def get_amount_inside(self,figure):
    figure.area=figure.width*figure.height
    self.area=self.width*self.height
    return(int(self.area/figure.area))
  
    
class Square(Rectangle):
  
  def __init__(self,side):
    self.width=side
    self.height=side

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self,side):
    self.side=side
    self.width=self.height=side
