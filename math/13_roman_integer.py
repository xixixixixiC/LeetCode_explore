class solution:
    def reverse(self,s:str)->int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=s.replace('IV','IIII').replace('IX','VIIII')
        s=s.replace('XL','XXXX').replace('XC','LXXXX')
        s=s.replace('CD','CCCC').replace('CM','DCCCC')
        sum=0
        for i in s:
            sum=sum+dict[i]
        return print(sum)

origi=input("Give a Ramans number:")
solu=solution()
solu.reverse(origi)

#runtime:60ms
#memory:13.4MB
#why input use "" double quate only instead of ''
