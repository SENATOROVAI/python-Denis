my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
values_list = [values for values in my_dict.values()]
values_list.sort()
biggest = values_list[-2:]
