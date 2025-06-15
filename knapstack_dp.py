coin=[2,3,4,5]
amt=12
if amt>sum(coin):
    print("np")
dp=[[0]*(amt+1) for i in range(len(coin))]
for i in range(len(coin)):
    dp[i][0]=1
dp[0][coin[0]]=1
for i in range(1,len(coin)):
    for j in range(1,amt+1):
        if j<coin[i]:
            dp[i][j]=dp[i-1][j]
        else:
            if dp[i-1][j]==1:
                dp[i][j]=dp[i-1][j]
            else:
                if dp[i-1][j-coin[i]]==1:
                    dp[i][j]=dp[i-1][j-coin[i]]
                    ''' or u can write this one line
            dp[i][j]=dp[i-1][j] or dp[i-1][j-coin[i]]'''
            
for i in dp:
    print(i)
if dp[-1][-1]==1:
    print("poss")
else:
    print("np")

