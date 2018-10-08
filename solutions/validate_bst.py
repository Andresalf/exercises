import sys
from data_types.bst import Bst, Node

'''
Valid:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7

Invalid:
      5
    /   \
   5     8
  / \   /
 4   9 7
'''
class BstValidate(Bst):

    CURRENT_INDEX = 2
    
    def validate(self):
        if not self.root:
            raise TypeError
        if not self.root.left and not self.root.right:
            return True
            
        circular_buffer = [-sys.maxsize, -sys.maxsize]
        buffer_index = 0
        
        return self.validate_helper(self.root, circular_buffer, buffer_index)
        
    def validate_helper(self, root, circular_buffer, buffer_index):
        if root:
            left_is_good = self.validate_helper(root.left, circular_buffer, buffer_index)
            if not left_is_good or root.data < circular_buffer[1 - buffer_index]:
                return False
                
            circular_buffer[buffer_index] = root.data
            buffer_index = 1 - buffer_index
            
            right_is_good = self.validate_helper(root.right, circular_buffer, buffer_index)
            
            return right_is_good
            
        return True
                    
                    