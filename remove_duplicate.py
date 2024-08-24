def del_duplicate():
    list = [1, 2, 2, 3, 3, 3, 4, 5]
    n = len(list)  # 7

    i = 0
    while i < n - 1:  # i<6, i is capped at 5
        j = i + 1  # j is capped at 6
        while j < n:  # j < 7
            if list[i] == list[j]:
                list.remove(j)
                n -= 1
            else:  # list[i]!=list[j]
                j += 1
        i += 1

    print(list)


del_duplicate()
