import sys
import math

def read_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def strings_to_float(nums):
    return [float(n) for n in nums]

def read_numbers():
    nums = read_lines( sys.argv[1])
    nums = [ strings_to_float(str(n).split()) for n in nums]
    return nums

def read_points():
    nums = read_lines( sys.argv[2])
    nums = [ strings_to_float(str(n).split()) for n in nums]
    print (nums)
    return nums



nums = read_numbers()
x = nums[0][0]
y = nums[0][1]
r = nums[1][0]
print(x, y, r)

points = read_points()

for point in points:
    lenght_square = (point[0] - x) ** 2 + (point[1] - y) ** 2

    if lenght_square > r ** 2:
        print("2")
        continue

    if lenght_square < r ** 2:
        print("1")
        continue

    print("0")
























