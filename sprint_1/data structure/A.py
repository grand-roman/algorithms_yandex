n = int(input())
s = []
for i in range(n):
    t = input()
    if t not in s:
        s.append(t)
        print(t) 
