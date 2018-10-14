from data_types.bst import Bst
from data_types.node import Node


class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
        if node:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node.data)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node:
            visit_func(node.data)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self,node, visit_func):
        if node:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node.data)