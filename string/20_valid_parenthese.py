#s= "()[]{}"
#s="{[]}"
s='(('
temp=[]
dic={'(':')', '[':']',  '{':'}'}
if len(s)%2!=0:
    print(False)
else:
    for ch in s:
        if ch in dic:#key in dic
            temp.append(ch)
        elif temp and ch==dic[temp[-1]]:
            temp.pop()
        else:
            print(False)
            break
    if temp:
        print(False)
    else:
        print(True)
