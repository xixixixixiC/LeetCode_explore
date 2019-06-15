class Solution:
    def reverse(self,x: int) -> int:
        num=0
        sign=1
        if x < 0:
            sign=-1
            x=abs(x)
        while x>0:
            gw=x%10
            x=x//10
            num=num*10+gw
        if num > (2**31-1):
            return print(0)
        else:
            return print(num*sign)

x=input("please input a number:")
x=int(x)

number=Solution()
number.reverse(x)
#runtime:40ms
#memory(13.2MB)
