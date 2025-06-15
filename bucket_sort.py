#bucket sort
'''
(3, 3)
(4, 2)
(2, 2)
(1, 1)
(8, 1)
(7, 1)
(9, 5)
(6, 1)
(5, 1)
[[], [1, 8, 7, 6, 5], [4, 2], [3], [], [9]]
[1, 8, 7, 6, 5, 4, 4, 2, 2, 3, 3, 3, 9, 9, 9, 9, 9]
'''
d={}
a=[3,4,2,4,3,1,2,3,8,7,9,9,6,5,9,9,9]
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
for i in d.items():
    b[i[1]].append(i[0])
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)
