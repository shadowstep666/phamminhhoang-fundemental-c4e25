chieucao = float(input(" nhap chieu cao :"))
weight = float(input(" nhap can nang : "))
height = chieucao / 100
print("height =" , height , "(M)")
print("weight =", weight , "(kg)")

BMI = weight / (height ** 2)
print("BMI" , BMI)

if BMI < 16 :
    print ("Severely underweight")
elif BMI < 18.5 :
    print("Underweight")
elif BMI < 25 :
    print("Normal")
elif BMI < 30 :
    print("Overweight")
else :
    print("obese")