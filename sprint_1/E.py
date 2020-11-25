a = int(input())
k=''
while a!=1:
    k= str(a%2) + k
    a//=2
print(str(a)+k)
