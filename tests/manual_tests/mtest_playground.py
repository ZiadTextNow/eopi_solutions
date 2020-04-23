import random

from matplotlib import pyplot
from arshan.problem_5_p_12_arshan import Problem5P12Arshan

if __name__ == '__main__':
    summations = []
    one = []
    two = []
    gran = 10000
    for _ in range(100000):
        dice1 = random.randint(1, gran)
        one.append(dice1)
        dice2 = random.randint(1, gran)
        two.append(dice2)
        summations.append(dice1 + dice2)
    _ = pyplot.hist(summations, bins=2*gran)
    _ = pyplot.hist(one, bins=2*gran)
    _ = pyplot.hist(two, bins=2*gran)
    pyplot.show()


