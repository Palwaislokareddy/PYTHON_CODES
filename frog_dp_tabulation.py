#normal recursion
a=[10,20,30,10,30,20,10]
'''def jump(i,a):
    if i==0:
        return 0
    if i==1:
        return abs(a[0]-a[1])
    l=jump(i-1,a)+abs(a[i-1]-a[i])
    r=jump(i-2,a)+abs(a[i-2]-a[i])
    return min(l,r)
n=len(a)
print(jump(n-1,a))


## in dp (memory)
def frog(n):
    if n<=1:
        return dp[n]
    dp[n]=min(frog(n-1)+abs(a[n]-a[n-1]),frog(n-2)+abs(a[n]-a[n-1]))
    return dp[n]
dp=[0,abs(a[1]-a[0]),0,0,0,0,0]
frog(6)
print(dp)

#in dp (tabulation)
n=[0,10]
for i in range(2,7):
    n.append(min(n[i-1]+abs(a[i]-a[i-1]),n[i-2]+abs(a[i]-a[i-1])))
print(n[7-1])'''

#----
'''
x=0
y=abs(a[1]-a[0])
for i in range(2,7):
    ans=min(y+abs(a[i]-a[i-1]),x+abs(a[i]-a[i-2]))
    x=y
    y=ans
print(y)'''


#-------------------------------for k jumps----------------------------------
dp=[9999]*len(a)
dp[1]=abs(a[0]-a[1])
k=2
for i in range(2,len(a)):
    for j in range(1,k+1):
        temp=dp[i-j]+abs(a[i]-a[i-j])
        dp[i]=min(temp,dp[i])
print(dp[len(a)-1])
    
    


    
    
    
