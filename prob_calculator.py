import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key in kwargs:
            for i in range(kwargs[key]):
                self.contents.append(key)

    def draw(self,draw_num):
        output = []
        for i in range(draw_num):
            rand_index = random.randint(0,len(self.contents)-1)
            output.append(self.contents[rand_index])
            self.contents.pop(rand_index)
            if not self.contents:
                break
        return output


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_times = 0
    expected_balls_list = []
    for key in expected_balls:
        for i in range(expected_balls[key]):
            expected_balls_list.append(key)
    for i in range(num_experiments):
        hat_cp = copy.deepcopy(hat)
        drawn_balls = hat_cp.draw(num_balls_drawn)
        try:
            for ball in expected_balls_list:
                drawn_balls.remove(ball)
        except (ValueError, AttributeError):
            continue
        else:
            success_times = success_times + 1
    return success_times/num_experiments
