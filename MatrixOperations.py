r1 = int(raw_input("\nEnter number of rows of matrix 1 : "))
c1 = int(raw_input("Enter number of columns of matrix 1 : "))

r2 = int(raw_input("\nEnter number of rows of matrix 2 : "))
c2 = int(raw_input("Enter number of columns of matrix 2 : "))


#______________________________
# creating matrices of size r*c
#------------------------------

Mat1 = [[0 for j in range(c1)]for i in range(r1)]
Mat2 = [[0 for j in range(c2)]for i in range(r2)]
Mat3 = [[0 for j in range(c2)]for i in range(r1)]
Mat4 = [[0 for j in range(c1)]for i in range(r1)]
Mat5 = [[0 for j in range(c1)]for i in range(r1)]
Mat6 = [[0 for j in range(r1)]for i in range(c1)]
Mat7 = [[0 for j in range(r2)]for i in range(c2)]

#_____________________________
# assigning values in matrices
#-----------------------------

print "\n\nInput values of matrix 1 below:\n"
for i in range(r1):
    for j in range(c1):
        Mat1[i][j] = int(raw_input("Enter the value at position "+"("+str(i)+","+str(j)+")"+" : "))

print "\nInput values of matrix 2 below:\n"
for i in range(r2):
    for j in range(c2):
        Mat2[i][j] = int(raw_input("Enter the value at position "+"("+str(i)+","+str(j)+")"+" : "))
        
#__________________
# printing matrices
#------------------

print "\n\nMatrix 1 is:"
for i in range(r1):
    for j in range(c1):
        print Mat1[i][j],
    print
    
print "\nMatrix 2 is:"
for i in range(r2):
    for j in range(c2):
        print Mat2[i][j],
    print

#____________________________________
# calculate transpose of two matrices
#------------------------------------

for i in range(c1):
    for j in range(r1):
           Mat6[i][j] += Mat1[j][i]

for i in range(c2):
    for j in range(r2):
           Mat7[i][j] += Mat2[j][i]

print "\n\nTranspose of the matrix 1 is:"
for i in range(c1):
    for j in range(r1):
        print Mat6[i][j],
    print

print "\nTranspose of the matrix 2 is:"
for i in range(c2):
    for j in range(r2):
        print Mat7[i][j],
    print

#__________________________________
# calculate product of two matrices
#----------------------------------

if c1!=r2 :
    print "\n\n***Matrices CANNOT be Multiplied***"
    print "\n\t_____________________"
    print "\tABORTING THE PROGRAM!"
    print "\t---------------------\n"
    flag=0
else :
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                Mat3[i][j] += Mat1[i][k] * Mat2[k][j] 
    flag=1                  
    print "\n\nProduct of these matrices is:"
    for i in range(r1):
        for j in range(c2):
            print Mat3[i][j],
        print

#____________________________________________________
# calculate addition and substraction of two matrices
#----------------------------------------------------

if flag!=0 :
    if r1!=c2 :
        print "\n\n**Matrices CANNOT be Added or Subtracted**"
        print "\n\t  _____________________"
        print "\t  Aborting the program!"
        print "\t  ---------------------\n"
    elif r1!=r2 :
        print "\n\n**Matrices CANNOT be Added or Subtracted**"
        print "\n\t  _____________________"
        print "\t  Aborting the program!"
        print "\t  ---------------------\n"
    elif c1!=c2 :
        print "\n\n**Matrices CANNOT be Added or Subtracted**"
        print "\n\t  _____________________"
        print "\t  Aborting the program!"
        print "\t  ---------------------\n"
    else:
        for i in range(r1):
            for j in range(c1):
                   Mat4[i][j] += Mat1[i][j] + Mat2[i][j]

        for i in range(r1):
            for j in range(c1):
                   Mat5[i][j] += Mat1[i][j] - Mat2[i][j]

        print "\n\nSum of these matrices is:"
        for i in range(r1):
            for j in range(c1):
                print Mat4[i][j],
            print
            
        print "\n\nDifference of these matrices is:"
        for i in range(r1):
            for j in range(c1):
                print Mat5[i][j],
            print
else :
    pass   
