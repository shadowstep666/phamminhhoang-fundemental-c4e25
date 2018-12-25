
xs = " * "
n= int(input("nhap vao n :"))
if (n%2) == 0:
    y=int(n/2)
    for i in range(y):
        print("x",end=(" "))
        print(xs,end=(" "))
else :
    y = int(n/2)+1
    for i in range(y) :
        print("x",end=(" "),)
        if i!= y - 1 :
            print(xs,end=(" "))
        else:
            print(" ")