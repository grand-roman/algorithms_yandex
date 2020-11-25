a = input()
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
a = list(b.items())
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j][1]>a[i][1]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        elif a[j][1]==a[i][1]:
            if a[j][0]<a[i][0]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
for i in a:
    print(i[0]*i[1],end='')
