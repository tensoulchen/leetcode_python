nums = [0,1,2,3,4,5,6,7,9]

def misssingNumber(nums):
    l=len(nums)
    numSum=(1+l)*l//2
    arrSum=sum(nums)
    return numSum-arrSum

print(misssingNumber(nums))