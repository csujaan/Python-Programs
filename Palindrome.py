n=int(raw_input("Enter The no:"))
n1=n
s=0
while n>0 :
    r=n%10
    s=s*10+r
    n=n/10
if s==n1:
    print "palindrome"
else:
    print"not palindrome"
