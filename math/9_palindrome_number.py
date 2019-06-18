#!/usr/bin/env python
# coding: utf-8

# In[3]:

class solution:
    def palindrome(self,x):
        if x<0:
            return print(False)

        dig=1
        while x/dig>=10:
            dig=dig*10

        while x:
            left=x//dig
            right=x%10
            if left!=right:
                return print(False)
            x=(x%dig)//10
            dig=dig/100

        return print(True)

x=int(input("please input a int number:"))
p=solution()
p.palindrome(x)
#runtime: 96ms
#memory: 13.4 MB
