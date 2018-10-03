from data_types.bst import Node, Bst

class Solution(Bst):

    def find_second_largest(self):
        if not self.root:
            raise TypeError
        if not self.root.left and not self.root.right:
            return self.root

        stack = [None, None]
        i = [0]
        self.find_second_largest_helper(self.root, stack, i)

        return stack[i[0] % 2]
        

    def find_second_largest_helper(self, root, stack, i):
        if root:
            self.find_second_largest_helper(root.left, stack, i)

            stack[i[0] % 2] = root
            i[0] += 1

            self.find_second_largest_helper(root.right, stack, i)            
        