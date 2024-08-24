#  to find two numbers that sum up to be ()

def two_sum(num, target):
    pairs = []

    # to remove duplicated numbers
    num = list(set(num))

    # to sort the num list
    num = sorted(num)  # 0, 1, 2, 4, 5, 6

    # two pointers approach
    n = len(num)  # 6

    left, right = 0, n-1

    while left < right:
        sum_of_two = num[left] + num[right]
        if sum_of_two == target:
            pairs.append((num[left], num[right]))
            left += 1
            right -= 1

        if sum_of_two <= target:
            left += 1

        else:
            right -= 1

    return print(pairs)


two_sum([0, 1, 6, 4, 2, 5, 2], 6)
