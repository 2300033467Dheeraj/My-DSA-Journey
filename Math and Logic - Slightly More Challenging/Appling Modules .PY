# Enter your code here. Read input from STDIN. Print output to STDOUT
mod = 10**9+7
a,b,c,d,e,f = map(int, input().split())
p1 = (((a%mod) * (b%mod)) % mod * (c%mod)) %mod
p2 = (((d%mod) * (e%mod)) % mod * (f%mod)) % mod
re = (p1-p2+mod)% mod
print(re)