num=int(input("Enter a number:"))
s1=str(num)
sum1=0
for i in range(len(s1)):
    if i % 2 != 0:
        if int(s1[i]) % 2 == 0:
            sum1 += int(s1[i])
 
print(sum1)