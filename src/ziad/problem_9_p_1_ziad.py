from protocol.problem_9_p_1 import Problem9P1
from protocol.problem_9_p_1 import BinaryTreeNode


class Problem9P1Ziad(Problem9P1):
  def height_balanced(self, binary_tree):
    # return self.height_balanced(binary_tree)
    return self.is_balanced_method_2(binary_tree)


  '''
    "The depth of a node n is the number of nodes on the search path from the root to n, not including n itself"
    "The height of a binary tree is the maximum depth of the nodes in that tree."

                                  2             depth = 0
                                /   \
                              1       3         depth = 1
                                        \
                                          4     depth = 2 => height = 2 

    Important to note with trees is that - although extra memory is not explicitly allocated - 
    the call stack depth of the recursive function is what ultimately determines the space allocated.
  '''

  def __height(self, root):
    return 1 + max(self.__height(root.left), self.__height(root.right)) if root else 0

  '''
    A binary tree is height-balanced if for each node in the tree, 
    the difference in the height of its left and right subtrees is at most one,
    (and the subtrees themselves are balanced). 
  '''

  # Method 1: At each node, determine the heights of its left and right subtrees, as well as if they are themselves balanced
  def is_balanced_method_1(self, root):
    if root is None:
      return True

    difference_between_subtree_heights = abs(self.__height(root.left) - self.__height(root.right))

    # We need to ensure that root's subtrees themselves are also balanced
    is_left_subtree_balanced = self.is_height_balanced(root.left)
    is_right_subtree_balanced = self.is_height_balanced(root.right)

    return is_left_subtree_balanced and \
           is_right_subtree_balanced and \
           difference_between_subtree_heights <= 1

  # Method 2
  def is_balanced_method_2(self, root):
    return True if self.__balanced_height(root) > -1 else False

  # Helper where the actual recursion happens
  # If the tree rooted at root is balanced, return its height
  # else, return -1 (flag) to inform this node's parent that this is an
  # unbalanced subtree
  def __balanced_height(self, root):
    # base case
    if root is None:
      return 0

    # height of the descendants
    left_height = self.__balanced_height(root.left)
    right_height = self.__balanced_height(root.right)

    # if either of the subtrees is unbalanced, make an early return
    # because we don't care about this tree's height
    if left_height == -1 or right_height == -1:
      return -1
    # Now that we know that both subtrees are balanced, we check the
    # height difference between them
    elif abs(left_height - right_height) > 1:
      return -1

    return max(left_height, right_height) + 1