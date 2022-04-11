import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls_hat):
        self.contents = []
        for key, value in balls_hat.items():
            print ("%s == %s" %(key, value))
            for i in range(0, int(value)):
                self.contents.append(key)
        print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
