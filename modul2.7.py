def print_params(a, b, c):
    print(a, b, c)

valuse_list2 = [54.32 , 'Str']
valuse_list = [1, '3', True]
valuse_dict = {'a': 2, 'b': 4, 'c': 5}
print_params(**valuse_dict)
print_params(*valuse_list)
print_params(*valuse_list2, 42)
