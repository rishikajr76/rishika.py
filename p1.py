import math
n = int(input("enter number:"))
root = math.sqrt(n)
root1 = int(root)
if root1 * root1 == n:
    print("Perfect square")
else:
    print("Not Perfect square")    