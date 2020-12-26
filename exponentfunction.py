def raise_to_power(base_num, pow_num):
    """
    This is an exponent function. It takes two variables and gives the result of the exponent of that number.
    :param base_num: this is the base number of the problem
    :param pow_num: this is the raised power of the base number.
    :return: returns the actual value after power being applied.
    """
    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result


base_input = input("Please enter base number: ")
pow_input = input("Please enter power: ")


print(raise_to_power(float(base_input), float(pow_input)))



'''
1 x 2    result = 2  range run 1
2 x 2    result = 4  range run 2
4 x 2    result = 8  range run 3
8 x 2    result = 16 range run 4
16 x 2   result = 32 range run 5

'''




