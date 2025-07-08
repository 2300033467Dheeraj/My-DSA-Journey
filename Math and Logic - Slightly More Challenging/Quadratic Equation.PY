import math
a, b, c = map(int,input().split())
Discriminant = b * b - 4 * a * c
if Discriminant > 0:
    Root1 = (-b + math.sqrt(Discriminant)) / (2*a)
    Root2 = (-b - math.sqrt(Discriminant)) / (2*a)
    print("{:.2f} {:.2f}".format(Root1,Root2))
elif Discriminant == 0:
    root = -b / (2 * a)
    print("f{:.2f} {:.2f}".format(root,root))

else:
    print("Imaginary Roots")
