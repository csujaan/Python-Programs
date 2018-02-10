n=int(raw_input("Enter The no:"))
s=0
for i in range(1,n-1):
    if n % i ==0:
        s=s+i
if s==n:
    print "perfect number"
else:
    print "not perfect number"
