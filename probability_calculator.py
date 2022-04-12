import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []

        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

        self.first_contents = copy.copy(self.contents)

    def draw(self, draw_nbr):
        self.draw_nbr = draw_nbr
        self.removed_balls = []

        if self.draw_nbr > len(self.contents):
            self.removed_balls = copy.copy(self.contents)

        else:
            for _ in range(draw_nbr):
                remove_ball = random.choice(self.contents)
                self.removed_balls.append(remove_ball)
                self.contents.remove(remove_ball)

        if len(self.contents)==0:
            self.contents=copy.copy(self.first_contents)

        return self.removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    wins = 0
    tot = 0
    for _ in range(num_experiments):
        contents_still = copy.copy(expected_balls)
        hat.contents=copy.copy(hat.first_contents)
        hat.removed_balls=hat.draw(num_balls_drawn)
        for color_ball,count_ball in expected_balls.items():
          for _ in range(count_ball):
            if color_ball in hat.removed_balls:
              hat.removed_balls.remove(color_ball)
              contents_still[color_ball]-=1

        if sum(v for v in contents_still.values())==0:
          wins += 1
          
    probability = wins / num_experiments

    return probability