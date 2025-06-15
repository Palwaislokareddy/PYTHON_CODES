#element with largest frequency
'''d=[2,13,4,2,9,9,5,8,7,13,3]
freq={}
k=3
for i in d:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
m=0
for v in freq:
    if freq[v]>m:
        m=freq[v]
        res=v
print(res)
m=max(d.values())'''

#element with kth largest frequency

a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
k=3
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
    b[d[i]]=i
print(b[-k])




    
    
    
    
    



    