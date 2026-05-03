sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)

j=1
while j<=9:
    k=1
    while k<=j:
        print(f'{k}x{j}={k*j}',end='\t')
        k+=1
    print()
    j+=1

for a in range(1,10):
    for b in range(1,a+1):
        print(f'{b}x{a}={a*b}',end='\t')
    print()