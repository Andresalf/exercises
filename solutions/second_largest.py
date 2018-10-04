from data_types.bst import Bst, Node

'''
Input:
                _10_
              _/    \_          
             5        15
            / \       / \
           3   8     12  20
          / \              \
         2   4             30


                _10
              _/              
             5      
            / \     
           3   7     
        
                _10_
              _/    \_          
             5        20
              \       /
               7     15
                    /
                   14
'''
class Solution(Bst):

    def find_second_largest(self):
        if not self.root:
            raise TypeError('root is None.')
        if not self.root.left and not self.root.right:
            raise ValueError('root must have at least one child node.')

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
        