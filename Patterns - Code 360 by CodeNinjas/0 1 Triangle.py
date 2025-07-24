n = 6
star = 1
for i in range(0,n):
    if i % 2 == 0:
        star = 1
    else:
        star = 0
    for j in range(0,i):
        star = 1 - star
        print(star, end="")
    print()