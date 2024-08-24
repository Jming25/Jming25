#  to find two numbers that sum up to be ()

def two_sum():
    num = [0, 1, 6, 4, 2, 5, 2]

    # to remove duplicated numbers
    num = list(set(num))

    # to sort the num list
    num = sorted(num)

    #
    n = len(num)
    target = 6
    
    for i in range(n-1):
        for j in range(i+1, n):  # note that it's NOT (i+1), this means end at i+i
            if num[i] + num[j] == target:
                print(num[i], num[j])


two_sum()
