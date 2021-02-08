"""
n = int(input("Input Integer"))

if n % 2 != 0:
    print("Weird")
else:
    if n > 20:
        print("Not Weird....")
    elif n >= 6:
        print("Weird")
    else:
        print("Not Weird")git
"""


class Solucion:
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        nums.sort()
        return nums


sol = Solucion
nums = [1, 1, 2]
nums = sol.removeDuplicates(sol,nums)
print(len(nums), [x for x in nums])
