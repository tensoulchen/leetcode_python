def findLengthOfLCIS(nums):
    anchor, ans = 0, 1
    for i in range(len(nums)):
        if i and nums[i - 1] >= nums[i]:
            anchor = i
        else:
            ans = max(ans, i - anchor + 1)
    return ans


nums = [5,5]

print(findLengthOfLCIS(nums))
