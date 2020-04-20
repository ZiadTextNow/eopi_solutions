from protocol.problem_8_p_6	import Problem8P6
from collections import deque

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Problem 8.6var1 was trivial so was not explicitly done. You do exactly same thing as in this solution except every other
level you just pop instead of popleft (use a stack instead of queue)
Problem 8.6var2 was trivial so was not explicitly done. You do exactly same thing as in this solution except at the end
you reverse the result list using a linear algorithm with no memory requirement like solution to problem 7.2
I wonder if this problem can be solved using a different approach (like using a different search)
Problem 8.6var3 was trivial so was not explicitly done. You do exactly same thing as in this solution except after the 
list is created for each level just take the average. 
"""


class Problem8P6Vlad(Problem8P6):
    def breadth_first_search(self, binary_tree):
        return self.bfs_with_queue(binary_tree)

    def bfs_with_queue(self, binary_tree):
        # create a queue
        dfs_list = []
        if not binary_tree:
            return dfs_list
        node_queue = deque([binary_tree])

        # use same queue for each level and keep emptying at the same time
        # in the book solution they iterate over each queue element twice while I only do it once. Both solutions are
        # still linear, but mine is slightly faster :P
        while node_queue:
            cur_level_list = []
            for i in range(len(node_queue)):
                cur_node = node_queue.popleft()
                cur_level_list.append(cur_node.data)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)
            dfs_list.append(cur_level_list)
        return dfs_list
