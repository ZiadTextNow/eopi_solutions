from protocol.problem_9_p_1 import Problem9P1
from protocol.problem_9_p_1 import BinaryTreeNode

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem9P1Vlad(Problem9P1):
    def height_balanced(self, binary_tree):
        return self.book_soln_with_one_return_var(binary_tree)

    """ 
    wanted to see if you could do this with just one variable instead of two like the book. It is possible shown
    below but is harder to understand I think so not ideal. However I think this same method can always be applied
    to any problem that has two distinct return times as defined by the problem. instead of returning two types
    you have checks to see if the returned type is one of the two. 
    """
    def book_soln_with_one_return_var(self, binary_tree):
        def inner_func(binary_tree):
            if not binary_tree:
                return 1
            right_tree_height = inner_func(binary_tree.right)
            left_tree_height = inner_func(binary_tree.left)

            height_diff = abs(left_tree_height - right_tree_height)
            if abs(height_diff) > 1 or not right_tree_height or not left_tree_height:
                return 0
            return max(left_tree_height, right_tree_height) + 1
        # inner_func needed to be used to adjust the final return height to True
        return True if inner_func(binary_tree) else False

    """
    my original solution is super messy and confusing lol. After reading the book solution I realized I only needed to
    pass in one argument into the method and not two(height is not required) however using one return variable was still
    enough to accomplish the goal without any runtime or memory trade offs as shown above.
    """
    def modified_post_order_walk(self, binary_tree):
        def check_for_height_diff_more_than_one(binary_tree, cur_height):
            right_tree_height = cur_height
            if binary_tree.right:
                right_tree_height = check_for_height_diff_more_than_one(binary_tree.right, cur_height + 1)
                if not right_tree_height:
                    return right_tree_height
            left_tree_height = cur_height
            if binary_tree.left:
                left_tree_height = check_for_height_diff_more_than_one(binary_tree.left, cur_height + 1)
                if not left_tree_height:
                    return left_tree_height

            height_diff = left_tree_height - right_tree_height
            if abs(height_diff) > 1:
                return False
            if not cur_height:
                return True
            return max(left_tree_height, right_tree_height)

        return check_for_height_diff_more_than_one(binary_tree, 0)




