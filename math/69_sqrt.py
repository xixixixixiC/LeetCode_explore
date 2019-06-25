class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid=l+(r-l)//2#key l+
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif mid*mid>x:
                r=mid
            else:
                l=mid+1#key +1

x=int(input())
s=Solution()
result=s.mySqrt(x)
print(result)
