n = int(input())
temp = n
sum = 0
while (temp):
    d = temp % 10
    temp = temp//10
    sum += d**3
if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")
