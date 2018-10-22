from nose.tools import assert_equal, assert_raises
from solutions.math_probability.check_prime import *


class TestMath(object):

    def test_check_prime(self):
        math = Math()
        assert_raises(TypeError, math.check_prime, None)
        assert_raises(TypeError, math.check_prime, 98.6)
        assert_equal(math.check_prime(0), False)
        assert_equal(math.check_prime(1), False)
        assert_equal(math.check_prime(2), True)
        assert_equal(math.check_prime(5), True)
        assert_equal(math.check_prime(7), True)
        assert_equal(math.check_prime(9), False)
        assert_equal(math.check_prime(11), True)
        assert_equal(math.check_prime(97), True)
        assert_equal(math.check_prime(51), False)
        assert_equal(math.check_prime(193), True)
        print('Success: test_check_prime')


def main():
    test = TestMath()
    test.test_check_prime()


if __name__ == '__main__':
    main()