# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n , r = map(int,input().split())
print(0 if r < 0 and r > n 
else math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))