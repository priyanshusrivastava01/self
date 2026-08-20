# EvenorOdd–(Subtract2Again&Againusingforloop)

n = int(input("Enter the Number:"))

n = abs(n)

for i in range(n // 2):
    n -= 2
    
if n == 0:
    print("Even")
else:
    print("Odd")