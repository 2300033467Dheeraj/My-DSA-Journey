# A B and X bookmark_borderYou are given two numbers A and B along with an integer X. In one operation you can do one of the following: 
# Set A = A + X and B = B - X 
# Set A = A - X and B = B + X
# Determine if you can make A and B equal after applying the operation any number of times (possibly zero). 

# Input Format
#  The first and only line of input contains three integers A, B, and X separated by a space.

# Output Format
#  For each test case, print YES if you can make A and B equal, otherwise NO. 

# Constraints
#  1 <= A, B, X <= 109

# Examples
# Input 1
#  6 8 1

# Output 1
#  YES

# Input 2
#  15 16 2

# Output 2
#  NO

a, b, x = map(int,input().split())
print("YES" if abs(a - b) % (2 * x) == 0 else "NO")