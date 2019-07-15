class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cut=False
        place=-1
        count=0
        for i in range(len(s)):
            if s[place]==' ':#要么没开始数，要么结束了
                if cut:
                    return count
                else:
                    place-=1
            else:
                cut=True
                count+=1
                place-=1
        if place<len(s):
            return count

ans=Solution()
print(ans.lengthOfLastWord(s="hello world a "))


#runtime:32ms
#memory:13.2mb



#two pointers method:
s="Hello World "
slow=-1
while slow>=-len(s) and s[slow]==' ':
    slow-=1
print(slow)


fast=slow


while fast>=-len(s) and s[fast]!=' ':
    fast-=1
print(fast)

print('length of the last word:',slow-fast)

#run time:32ms
#memory:13.2mb
