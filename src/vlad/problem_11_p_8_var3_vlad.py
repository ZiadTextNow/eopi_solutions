from protocol.problem_11_p_8_var3 import Problem11P8Var3
import random
import operator
import collections

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Not sure why book soln wouldn't work? Mine doesn't work cuz I use greater than or equal too compare but theirs is fine
cuz they use just greater than. If you use equal to you get stuck in infinite loop

"""


class Problem11P8Var3Vlad(Problem11P8Var3):
    def place_the_mailbox(self, buildings):
        return self.divide_and_conquer(buildings)

    class TotalResNDist(object):
        def __init__(self, num_of_residents=0, distance_to_mailbox=0):
            self.num_of_residents = num_of_residents
            self.distance_to_mailbox = distance_to_mailbox

    def divide_and_conquer(self, buildings):
        # this simply return a TotalResNDist object for buildings before, at and after the mailbox
        def get_totals(mailbox_distance):
            new_total_before_box = self.TotalResNDist(0, 0)
            new_total_res_at_box = 0
            new_total_after_box = self.TotalResNDist(0, 0)
            for building in buildings:
                if building.distance < mailbox_distance:
                    new_total_before_box.num_of_residents += building.num_of_residents
                    new_total_before_box.distance_to_mailbox += building.num_of_residents * (
                            mailbox_distance - building.distance)
                elif building.distance == mailbox_distance:
                    new_total_res_at_box = building.num_of_residents
                else:
                    new_total_after_box.num_of_residents += building.num_of_residents
                    new_total_after_box.distance_to_mailbox += building.num_of_residents * (
                            building.distance - mailbox_distance)
            return new_total_before_box, new_total_res_at_box, new_total_after_box

        # returns the total distance to the mailbox after increasing mailbox distance by one
        def get_total_after_box_inc(total_before_box, total_res_at_box, total_after_box):
            new_total_dist_before_box = total_before_box.distance_to_mailbox + total_before_box.num_of_residents + total_res_at_box
            new_total_dist_after_box = total_after_box.distance_to_mailbox - total_after_box.num_of_residents
            return new_total_dist_before_box + new_total_dist_after_box

        start_dist, end_dist = 0, max(buildings).distance
        while True:
            mailbox_distance = random.randint(start_dist, end_dist)
            total_before_box, total_res_at_box, total_after_box = get_totals(mailbox_distance)

            cur_total_distance = total_before_box.distance_to_mailbox + total_after_box.distance_to_mailbox

            # check if increasing or decreasing mailbox distance by 1 will improve total distance
            total_distance_after_plus1 = get_total_after_box_inc(total_before_box, total_res_at_box,
                                                                 total_after_box)
            total_distance_after_minus1 = get_total_after_box_inc(total_after_box, total_res_at_box,
                                                                  total_before_box)
            if total_distance_after_plus1 < cur_total_distance:
                start_dist = mailbox_distance + 1
            elif total_distance_after_minus1 < cur_total_distance:
                end_dist = mailbox_distance - 1
            else:  # this is for cases when move the mailbox will make total distance worse or equal to current
                return mailbox_distance
