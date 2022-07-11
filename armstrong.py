a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    l = len(str(i))
    s = 0
    n = i
    for j in range(l):
        m = n % 10
        n = n // 10
        s = s + m ** l
    if i == s:
        print(i)
    else:
        count += 1
if count != 0:
    print("No Armstrong numbers in between the given numbers")
