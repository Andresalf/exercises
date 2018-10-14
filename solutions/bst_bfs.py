from data_types.bst import Bst
from data_types.node import Node

class BstBfs(Bst):

    def bfs(self, visit_func):
        if self.root:
            queue = []
            queue.append(self.root)
            while queue:
                current = queue.pop(0)
                visit_func(current.data)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            