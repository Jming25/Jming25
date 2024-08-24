def is_subsequence():  # to check whether list2 is in lis1

    word = "abn"
    word1 = "banana"
    word2 = "abandon"

    #  turn word into list
    normal_list = list(word)
    list1 = list(word1)
    list2 = list(word2)

    #  to check, use "all" function
    # checking whether "abn" is inside "abandon"
    if all(elem in normal_list for elem in list2):
        return print("True")

    else:
        print("False")

    # checking whether "abn" is inside "banana"
    if all(elem in normal_list for elem in list1):
        return print("True")

    else:
        print("False")


is_subsequence()

# notes
# "all" function returns True if all targeted values are found
# "all" function also returns True If the iterable object is empty
