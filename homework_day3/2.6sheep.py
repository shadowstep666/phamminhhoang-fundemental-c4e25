size = [ 5 ,7,300 , 90 ,24,50,75]

print("Hello , my name is hiep and these are my sheep size :")
print(size)
print(" now my biggest sheep  has size",max(size), " let's shear it")
x = size.index(max(size))
size[x]=8
print("after shearing , here is my flock")
print(size)



month = int(input(" nhap vao so thang thu hoach :"))
for i in range (month):
    print("month",i+1,":") 
    x = 0
    y = int(len(size))
    for j in range(y):
        size[x]=size[j]+50
        x+=1
    print("one month has pass , now here is my flock")
    print(size)
    if i < month-1 :
        print(" now my biggest sheep  has size",max(size), " let's shear it")
        x = size.index(max(size))
        size[x]=8
        print("after shearing , here is my flock")
        print(size)
    else :
        sum = 0
        for k in range(y):
            sum += size[k]
        print("my flock is total",sum)
        money = sum * 2
        print("I would get" , sum , " *2$=", money,"$" )





    

