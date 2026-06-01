cost = [1,100,1,1,1,100,1,1,100,1]

dp = [0] * (len(cost)+1)

dp[0] = cost[0]
dp[1] = cost[1]

for i in range(2,len(cost)):
    dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

print(dp[len(cost)-1])