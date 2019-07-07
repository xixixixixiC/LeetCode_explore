nums=[-2,1,-3,4,-1,2,1,-5,4]
#nums=[1,-1,1]
#nums=[-2,-1]
#nums=[-2,1]
cursum=maxsum=nums[0]
for number in nums[1:]:
    cursum=max(cursum+number,number)
    maxsum=max(cursum,maxsum)
print(maxsum)
#runtime:44ms
#memory:13.8mb
