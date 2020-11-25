a = input()
b = input()
asum = 0
bsum = 0
for i in a:
    asum+=ord(i)
for i in b:
    bsum+=ord(i)
print(chr(max(asum,bsum)-min(asum,bsum)))
