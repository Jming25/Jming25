#  to remove letters from the list above
#  to find the num closest to zero

def closest_num_to_zero():
    num = [7, 2, "B", 3, -1, 1, 4, 5, "a"]
    num = [x for x in num if isinstance(x, int)]
    # isinstance, a function to check variable types

    print("unsorted: ",num)  # unsorted

    sorted_list = sorted(num)  # sorted
    print("sorted: ",sorted_list)

    if sorted_list[0] * -1 == sorted_list[1]:
        print("The number closest to zero are ", sorted_list[0], " and ", sorted_list[1])
    # check if the modulus of first two numbers are equal

    else:
        print("The number closest to zero is ", sorted_list[0])
        # to print the num closest to zero


closest_num_to_zero()
#  run function
