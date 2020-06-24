def threeSumCloest(nums, target: int) -> int:
    length = len(nums)
    min = float('inf')  # 最小差值=三个数和-target；float('inf)正无穷
    for i in range(length - 1):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                if abs(nums[i] + nums[j] + nums[k] - target) < abs(min):
                    min = nums[i] + nums[j] + nums[k] - target
    return min + target  # 返回三数之和=最小差值+target

nums = [-1, 2, 1, 0]
target = 2
print(threeSumCloest(nums, target))
