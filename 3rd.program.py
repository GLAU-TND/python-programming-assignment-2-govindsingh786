a=0
b=int(input())
lst1=[]
c=0
str1=bin(b)
for in str1[2:]:
    if i=='1':
        c=c+1
    if i=='0':
        if c>a:
            lst1.append(c)
            c=0
        if c==len(str)-2:
            lst1.append(c)
print(max(lst1))
    
