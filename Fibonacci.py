n=int(raw_input("Enter the upper limit:"))
a=0
b=1
print a,b
for i in range(1,n):
    sum=a+b
    print sum
    a=b
    b=sum
