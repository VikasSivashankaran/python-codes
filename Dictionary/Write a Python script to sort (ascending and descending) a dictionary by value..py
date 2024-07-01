def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 5}

sorted_dict_asc = sort_dict_by_value(my_dict, reverse=False)
print("Dictionary sorted by value in ascending order:", sorted_dict_asc)

sorted_dict_desc = sort_dict_by_value(my_dict, reverse=True)
print("Dictionary sorted by value in descending order:", sorted_dict_desc)