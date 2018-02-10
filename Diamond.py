x="DIAMOND"
y=" "
ln=len(x)
for i in range(0,ln/2+1):
    for j in range (0, ln/2+1-i):
        print x[j],
    for n in range (0, 2*i-1):
        print y,
    if i <> 0 :
        for k in range (ln-j-1, ln):
           print x[k],
    else :
        for k in range (ln-j, ln):
           print x[k],
    print
for i in range(1,ln/2+1):
    for j in range (0, i+1):
        print x[j],
    for n in range (0
                    , ln/2-2*(i-1)):
        print y,
    if i <> ln/2 :
        for k in range (ln-j-1, ln):
           print x[k],
    else :
        for k in range (ln-j, ln):
           print x[k],
    print    
