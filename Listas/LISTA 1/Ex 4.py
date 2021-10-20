a = int(input())
b = int(input())
c = int(input())
h = int(input())

x = (a + b + (abs(a - b))) / 2
y = (x + c + (abs(x - c))) / 2
k = y*h

print(int(k))