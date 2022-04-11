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

    def draw(self, nrball):
        if nrball >= len(self.contents):
            return self.contents
        
        remove_balls = []
        for i in range(nrball):
            # remove balls self.contents[] and add to remove_balls[]
            random_ball = int(random.random() * len(self.contents))
            remove_balls.append(self.contents.pop(random_ball))
        print(remove_balls)
        print(self.contents)
        return remove_balls   

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(f"hat:................ {hat}")
    print(f"expected_balls:..... {expected_balls}")
    print(f"num_balls_drawn:.... {num_balls_drawn}")
    print(f"num_experiments:.... {num_experiments}")

    probability = 0

    return probability