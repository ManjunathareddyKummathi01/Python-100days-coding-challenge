%%writefile logical.py
a=5
b=6
c=10
if a>b and a>c:
  print("a is big")
elif b>c:
    print("b is big")
else:
    print("c is big")

%%writefile logical1.py
n=2030
if n%4==0 and n%100 !=0 or n%400==0:
      print("its A LEAP YEAR")
else:
    print("not a leap year")

%%writefile bmi.py
height=float(input("enter height in cm"))
weight=float(input("enter weight in kgs"))
bmi=(weight/height)*100
if bmi<=18.4:
  print("it's underweight")
elif bmi>18.5 or bmi < 24.9:
    print("it's normal")
elif bmi>25 or bmi<39.9:
    print("it's overweight")
else:
    print("it's obese")


%%writefile bit.py
a=100
b=10
print(a&b)

%%writefile bit1.py
a=100
b=50
print(a|b)



%%writefile bit2.py
a=5
b=10
print(~a)
print(a^b)


%%writefile implicit.py
x=10
print(type(x))
y=5.86
print(type(x))
z=x+y
print(z)
print(type(z))


%%writefile explicit.py
x=10
print(type(x))
y=5.86
print(type(x))
z=int(x+y)
print(z)
print(type(z))

