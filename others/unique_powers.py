
def get_num_powers(x, n, num=1):
    power = num**n
    if power < x:
        return get_num_powers(x, n, num+1) + get_num_powers(x-power, n, num+1)
    elif power == x:
        return 1

    return 0


print(get_num_powers(10, 2))
print(get_num_powers(100, 3))
print(get_num_powers(100, 2))