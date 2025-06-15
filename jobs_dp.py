a=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
s=[5,6,5,4,11,2]
n=len(s)
dp=s.copy()
def jobs():
    for j in range(1,len(s)):
        for i in range(0,j):
            if a[i][1]<=a[j][0]:
                dp[j]=max(s[j]+dp[i],dp[j])
    print(dp[len(s)-1])    
jobs()
            
            
        
