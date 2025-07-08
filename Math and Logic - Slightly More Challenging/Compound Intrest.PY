P, R, N, T = map(int,input().split())
Compound_Interest = P * (1 + (R//N)) ** (N * T) - P
print(int(Compound_Interest))