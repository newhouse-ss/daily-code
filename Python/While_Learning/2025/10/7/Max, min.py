nums = [1, 2, 3, 4, 5]
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums, reverse = True))

print(nums.sort(reverse = True))#会输出None，原因是nums.sort()做的是原址修改，不会返回任何值，sorted()会返回一个新的list
nums.sort(reverse = True)
print(nums)

reversed_nums = reversed(nums)#reversed返回的是逆序后数组的地址
print(reversed_nums)