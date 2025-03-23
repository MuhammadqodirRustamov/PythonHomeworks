num = int(input("Enter a positive integer: "))
for i in range(1, int(num/2)+1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")
print(f"{num} is a factor of {num}")