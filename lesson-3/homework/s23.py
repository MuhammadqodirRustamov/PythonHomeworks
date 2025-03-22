import random

start = 12
end  = 20
count = 5

s = set()

for i in range(0, count):
    n = random.choice(range(start, end))
    s.add(n)
print(s)