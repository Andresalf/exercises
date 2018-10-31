from math import sqrt


class Math(object):

    def check_prime(self, num):
        if num is None or type(num) is not int:
            raise TypeError
        if num == 2 or num == 3:
           return True
        if num < 2 or num % 2 == 0:
            return False
            
        for i in range(3, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
                
        return True