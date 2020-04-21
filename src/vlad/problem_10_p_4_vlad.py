from protocol.problem_10_p_4 import Problem10P4
import heapq
import math

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem10P4Vlad(Problem10P4):
    def k_closest_stars(self, stars, k):
        return self.max_heap_method(stars, k)

    def max_heap_method(self, stars_coord, k):
        class Star(object):
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

            @property
            def distance(self):
                return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

            def __lt__(self, distance):
                return self.distance < distance

        stars = []
        for star_coord in stars_coord:
            stars.append(Star(*star_coord))

        max_heap = []
        for star in stars:
            heapq.heappush(max_heap, (-star.distance, star))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[star.x, star.y, star.z] for _, star in heapq.nlargest(k, max_heap)]




