n = 153
n = str(n)
count = 0
for num in n:
    count += int(num) ** len(n)
    
if count == int(n):
    print("Arm strong")
else:
    print("not")