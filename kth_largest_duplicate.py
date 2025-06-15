#find the kth largest element considering the duplicates
'''a=[3,4,2,4,3,1,2,3,8,7,9,9,6,5,9,9,9]
k=3
n=max(a)
b=[]
for i in range(n+1):
    b.append(0)

for i in a:
    b[i]+=1
for i in range(len(b)-1,-1,-1):
    if b[i]!=0:
        k-=b[i]
    if k<=0:
        print(i)
        break'''
a=[3, 4, 2, 4, 3, 1, 2, 3, 8, 7, 9, 9, 6, 5, 9, 9, 9]
k=3
freq={}
for i in a:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for num in range(max(freq.keys()), min(freq.keys())-1,-1):
    if num in freq:
        k-=freq[num]
        if k<=0:
            print(num)
            break

    
