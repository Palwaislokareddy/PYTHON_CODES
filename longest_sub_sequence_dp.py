s="ababd"
m="aacbd"
s1=len(s)+1
s2=len(m)+1
dp=[[0]*s1 for _ in range(s2)]
for i in range(1,s2):
    for j in range(1,s1):
        if m[i-1]==s[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
for i in dp:
    print(i)
print(dp[-1][-1])       

