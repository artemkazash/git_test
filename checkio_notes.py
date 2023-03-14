def fabi(num):
    a=0
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b+=temp

for i in fabi(20):
    print(i)
