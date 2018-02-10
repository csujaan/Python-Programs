x="TIGPS"
y=" "
ln=len(x)
d=ln/2
u=ln/2+1
for i in range(1,ln-1):
    
    for n in range (0, ln-i):
        print y,
    
    for k in range (d,u):
         print x[k],
    d=d-1
    u=u+1

        
    print    
