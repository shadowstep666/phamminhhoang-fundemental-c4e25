items = [ "t-shirt","Sweater"]
while True :
    n= input("welcome to our shop , what do you want ( C , R , U , D )?")
    if n == "C" or n == "c" : # create new items
        y=str(input("create new item : "))
        items.append(y)
        print("our item:",items)
    elif  n == "R" or  n == "r": # read all items
        print(print("our item:",items))
    elif n == "U" or n == "u":# update new item
        x = int(input("Update position ?"))
        y = str(input(" new item ? "))
        items[x-1]= y
        print(print("our item:",items))
    elif n == "D" or n== "d": # delete items
        z = int(input(" delete position ? "))
        items.pop(z-1)
        print(print("our item:",items))

