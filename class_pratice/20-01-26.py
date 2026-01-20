a = int(input("Enter a Number: "))
num = []

for i in range(1, a+1):
    if i % 2 == 0:
        num.append(i)
    else:
        num.append("*")
        
print(num)