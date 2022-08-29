import copy
from importlib.resources import contents
import random

class Hat:
    def __init__(self, **input):
        contents = []
        for k, v in input.items():
            for i in range(v):
                contents.append(k)    
        self.contents = contents

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            pull = random.sample(self.contents, len(self.contents))
            self.contents = []
        else:
            pull = random.sample(self.contents, num_balls_drawn)       
            for each in pull:
                self.contents.remove(each)
        return pull   


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0   
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        reqts = []
        single_draw = hat_copy.draw(num_balls_drawn)

        for k, v in expected_balls.items():
            draw_count = single_draw.count(k)
            if draw_count >= v:
                reqts.append('success')
            else:
                reqts.append('fail')
        
        if 'fail' in reqts:
            m = m
        else:
            m += 1
    return(m/num_experiments)       

