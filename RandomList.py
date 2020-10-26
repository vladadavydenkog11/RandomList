import random

def compare():
    list1 = list([random.randint(0, 50) for i in range(1, 10)])
    print(list1)
    list2 = list([random.randint(0, 50) for j in range(1, 15)])
    print(list2)
    list3 = list()
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
    print(list3)


compare()
