#coin sum possible or not for infinity
coin=[2,3,4,5]
amt=12
dp=[[0]*(amt+1) for i in range(len(coin))]
for i in range(len(coin)):
    dp[i][0]=1
for i in range(0,len(coin)):
    for j in range(1,amt+1):
        if j<coin[i]:
            dp[i][j]=dp[i-1][j]
        elif dp[i-1][j]==1:
            dp[i][j]=dp[i-1][j]
        elif dp[i][j-coin[i]]==1:
            dp[i][j]=dp[i][j-coin[i]]
for i in dp:
    print(i)
