from data_types.bst import Node, Bst


class Solution(Bst):

    def find_second_largest(self):
        return self.find_second_largest_helper(self.root)
        
    def find_second_largest_helper(self, root):
        if not self.root:
            raise TypeError
        if not self.root.left and not self.root.right:
            return self.root.parent
        if self.root.right:
            return self.find_second_largest_helper(self.root.right)
        return self.find_second_largest_helper(self.root.left)
        