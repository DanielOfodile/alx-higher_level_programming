def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            i = replace
    return my_list
