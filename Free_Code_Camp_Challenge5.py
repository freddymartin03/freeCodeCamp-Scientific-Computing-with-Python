import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents += [ball] * count

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            for _ in range(num_balls):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn_balls.append(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}
        for ball in drawn_balls:
            drawn_dict[ball] = drawn_dict.get(ball, 0) + 1

        success = True
        for ball, count in expected_balls.items():
            if ball not in drawn_dict or drawn_dict[ball] < count:
                success = False
                break

        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability


hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "green": 2}, num_balls_drawn=4, num_experiments=10000)
print("Probability:", probability)

