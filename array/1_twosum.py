#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        if len(nums)<=1:
#            return False
#        dic={}
#        for i in range(len(nums)):
#            if nums[i] in dic:
#                return  [dic[nums[i]],i]
#            else:
#                dic[target-nums[i]]=i
#class form code cannotrun, as List  is not defined. why????

number=input("a list of number with comma:")
nums=list(map(int,number.split(',')))
target=int(input("target:"))

if len(nums)<=1:
    print (False)
dic={}
for i in range(len(nums)):
    if nums[i] in dic:
        print ([dic[nums[i]],i])
    else:
        dic[target-nums[i]]=i
