%%writefile leetcode1.py
def sum(nums):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return i,j

k=[2,5,9,70,56]
target=14
x=sum(k)
print(x)

%%writefile con.py
age=int(input("enter your AGE:"))
if age>18:
    print("your eligible to vote")
else:
    print("your not eligible to vote")

%%writefile con1.py

print("*******welcome to park*******")
age=int(input("enter your AGE:"))
if age<18:
    print("your prohibited")

elif age>25 and age<35:
    print("your partially allowed")
elif age>35 and age<60:
    print("you can enjoy every where")
else:
    print("no entry")


%%writefile pat1.py
n=5
for i in range(0,n,1):
    for j in range(i,n,1):
        print(j,end="")
    print( "")

