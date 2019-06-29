class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target>nums[len(nums)-1]:
            return len(nums)
        elif target==nums[len(nums)-1]:
            return len(nums)-1
        elif target<nums[0]:
            return 0
        else:
            for i in range(len(nums)-1):
                if nums[i]<target<nums[i+1]:
                    return i+1
                elif target==nums[i]:
                    return i

nums=[1,3,5,6]
target=int(input("please input a number:"))
s=Solution()
print(s.searchInsert(nums,target))

# the  code is written by myself, but the code seems not pretty to me.
#runtime:36ms
#memory:13.6
