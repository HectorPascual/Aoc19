def check_increase(num):
    """
    Checks that going from left to right, the digits never decrease
    :param num:
    :return: True if the num match the condition or false if it decreases
    """
    prev = 0
    for i in str(num):
        if int(i) >= prev:
            prev = int(i)
        else:
            return False
    return True


def check_adjacency(num):
    """
    Checks that wo adjacent digits are the same (like 22 in 122345)
    :param num:
    :return:
    """
    for i in str(num):
        if str(num).count(i) > 1 and str(num)[str(num).index(i)+1] == i:
            return True
    return False


def count_passwords(array):
    return len(list(filter(lambda x: check_adjacency(x) and check_increase(x), array)))


input = [i for i in range(273025, 767253)]
print(count_passwords(input))
