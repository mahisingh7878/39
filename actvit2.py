#take  number from user 
num1=int(input("enter hight  "))
num2=int(input("enter weight "))

bmi=num2/(num1/100)**2

if bmi<=18.4:
    print("you are underweight",bmi)
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=34.9:
    print("you are  severly over weight")
elif bmi<=37.9:
    print("you are obese")
else: # when statement is false 
    print("you are severly over weight")



