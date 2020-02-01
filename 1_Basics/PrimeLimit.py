start = int(input('Enter the starting limit'))
end = int(input('Enter the end limit'))
print('prime numbers between ', start, ' and ', end, ' are :')

while start<end:
    flag=0
    i=2
    while i<=start//2:
        if start%i==0:
            flag=1
            break

    if flag==0:
        print(start)
    start=start+1








