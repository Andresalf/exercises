from nose.tools import assert_equal, assert_raises
from solutions.second_largest import *


class TestBstSecondLargest(object):
    def test_bst_second_largest(self):
        bst = Solution(None)
        assert_raises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        assert_equal(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        assert_equal(bst.find_second_largest(), node7)
        root = Node(10)
        bst = Solution(root)
        node20 = bst.insert(20)
        node5 = bst.insert(5)
        node7 = bst.insert(7)
        node15 = bst.insert(15)
        node14 = bst.insert(14)
        assert_equal(bst.find_second_largest(), node15)
        
        root = Node(10)
        bst = Solution(root)
        node20 = bst.insert(20)
        node15 = bst.insert(15)
        node14 = bst.insert(14)
        node13 = bst.insert(13)
        node21 = bst.insert(21)
        node23 = bst.insert(23)
        assert_equal(bst.find_second_largest(), node21)
        
        print('Success: test_bst_second_largest')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()


if __name__ == '__main__':
    main()