def island_water(m,i=0,j=0,n=None):
    if n==None:
        n=len(m)
    if i>=n or j>=n or i<0 or j<0 or m[i][j]==0 or m[i][j]==2 :
        return 0
    if m[i][j]==1:
        m[i][j]=2
    island_water(m,i-1,j,n)
    island_water(m,i+1,j,n)
    island_water(m,i,j+1,n)
    island_water(m,i,j-1,n)
m=[]
n=int(input())
for _ in range(n):
    m.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            
            island_water(m,i,j,n)
            c+=1       
print(c)
            
            
        
            


