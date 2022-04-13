import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for key, value in kwargs.items():
      #print ("%s == %s" %(key, value))
      for i in range(0,int(value)):
        self.contents.append(key)
    
  def draw(self, nrball):
    
    if nrball >= len(self.contents):
      # return "ALL" the balls
      random_ball = copy.deepcopy(self.contents)
    else: 
      # random balls from the contents
      # return those balls as a list of strings.
      random_ball = random.sample(self.contents, nrball)

    for ball in random_ball:
      # remove balls at random from contents 
      self.contents.remove(ball)

    return random_ball

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  got_expect_balls_M = 0

  # perform n experiments
  for i in range(num_experiments):
  
    # starting with a hat containing the specified balls
    hat_copied = copy.deepcopy(hat)

    # obtaining the drawn colors
    colors_draw = hat_copied.draw(num_balls_drawn)

    draw_color = True

    # checking the balls that were drawn
    for expected_color in expected_balls.keys():

      # if the amount of colors obtained in the draw is less than 
      # the expected amount, go to the next experiment
      if (colors_draw.count(expected_color)) < expected_balls[expected_color]:
        draw_color = False
        break

    if draw_color == True:
      got_expect_balls_M += 1
 
  probability = got_expect_balls_M / num_experiments
  
  return probability
