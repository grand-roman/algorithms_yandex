input()
x=input().split(' ')
k=int(input())
print(' '.join(list(str(int(''.join(map(str, x))) + k))))
