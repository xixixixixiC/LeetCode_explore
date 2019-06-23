a=input("binary number of a:")
b=input("binary number of b:")
#def addbinary(a:str,b:str)：
a_long=len(a)-1
b_long=len(b)-1
carry=0
result=''
while a_long>=0 or b_long>=0 or carry:#carry=0 is false
    currentvalue=(a_long>=0 and a[a_long]=="1")+(b_long>=0 and b[b_long]=='1') #b的内容还是字符串，所以要“”
    carry,remain=divmod(currentvalue+carry,2)
    result=str(remain)+result
    a_long=a_long-1
    b_long=b_long-1
print(result)
