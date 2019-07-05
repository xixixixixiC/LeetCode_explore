nums=[0,0,1,1,1,2,2,3,3,4]


#right way2, but a tricky way1:40ms
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
	        if(nums[i]!=nums[i+1]):
		        nums[x] = nums[i+1]
		        x+=1
        return len(nums[:x])







#two indexes way:64ms
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=1
        while j<len(nums):
            if nums[i-1]!=nums[j]:
                nums[i]=nums[j]
                i=i+1
            j=j+1
        return i


#right:way1,but del is bad usage:time limit exceeded 不好
i=0
while i < len(nums)-1:
    if nums[i]==nums[i+1]:
        del nums[i]
        i=i-1
    i=i+1
print(len(nums))
