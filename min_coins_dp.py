#min no of coins to get the ammount
coin=[2,3,4,5]
amt=12
if amt>sum(coin):
    print("not poss")
dp=[[0]*(amt+1) for i in range(len(coin))]
dp[0][coin[0]]=1
for i in range(1,len(coin)):
    for j in range(1,amt+1):
        if j==coin[i]:
            dp[i][j]=1
        elif j<coin[i]:
            dp[i][j]=dp[i-1][j]
        elif dp[i-1][j]!=0 and dp[i-1][j-coin[i]]!=0:
            dp[i][j]=min(dp[i-1][j], dp[i-1][j-coin[i]]+1)
        elif dp[i-1][j-coin[i]]!=0:
            dp[i][j]=dp[i-1][j-coin[i]]+1
        elif dp[i-1][j]!=0:
            dp[i][j]=dp[i-1][j]           
for i in dp:
    print(i)
print(dp[-1][-1])

            
    
