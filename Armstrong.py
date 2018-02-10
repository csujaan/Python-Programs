n=int(raw_input("Enter the Number : "))
a=n/100
c=n%10
b=(n%100-c)/10
m=(a**3)+(b**3)+(c**3)
if n==m:
    print n, "is an Armstrong number"
else:
    print n, "is not an Armstrong number"
