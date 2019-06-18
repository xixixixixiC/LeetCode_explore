
def isPalindrome(x):
    if x < 0:
        return print(False)
    p, rev = x, 0
    while p:
        rev = rev * 10 + p % 10
        p = p//10
    if rev == x:
        return print(True)
    else:
        return print(False)

x=int(input("a int number:"))
isPalindrome(x)
