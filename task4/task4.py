import sys
import math

def read_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def read_numbers():
    nums = read_lines( sys.argv[1])
    nums = [int(n) for n in nums]
    return nums


nums = read_numbers()



result_digit = round(sum(nums)/len(nums))
count = 0
for id, i in enumerate(nums):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
             i -= 1
             count += 1
        else:
            nums[id] = i

print(count)
