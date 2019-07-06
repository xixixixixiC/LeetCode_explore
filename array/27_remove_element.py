class Solution:
    def removeElement(self, nums, val: int) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                 nums[j]=nums[i]
                 j=j+1
        return j, nums[:j]

arr=[0,1,2,2,3,0,4,2]
val=2
s=Solution()
print(s.removeElement(arr,val))






# this is truelly the first time I finished a complete coding in LeetCode
#run time 32 ms
#memory:13.1MB
#I still have a question, why the elements in the output in non-ordered, that is the order is different, but they are both accepted
