def add_to_list(lst=[]):
    elem = input("Write an element: ")
    elem2 = input("Write another element: ")
    lst.append(elem)
    lst.append(elem2)
    return lst
a = []
add_to_list(a)
print(a)