h = [2,7,9,3,1]

dp = [0] * (len(h)+2)

for i in range(len(h)-1,-1,-1):
    take = h[i] + dp[i+2]
    skip = dp[i+1]
    dp[i] = max(take,skip)
    
print(dp[0])