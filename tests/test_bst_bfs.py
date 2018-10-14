from nose.tools import assert_equal
from solutions.bst_bfs import *


class TestBfs(object):

    def __init__(self):
        self.results = []

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(lambda elem: self.results.append(elem))
        assert_equal(str(self.results), '[5, 2, 8, 1, 3]')
        
        self.results = []
        bst = BstBfs(Node(10))
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(6)
        bst.insert(14)
        bst.insert(16)
        bst.bfs(lambda elem: self.results.append(elem))
        assert_equal(str(self.results), '[10, 5, 15, 3, 6, 14, 16]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()