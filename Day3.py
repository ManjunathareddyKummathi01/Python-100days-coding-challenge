%%writefile numbers.py
s="5"
print(type(s))
c=ord(s)
print(c)
print(type(c))

c=hex(30)
print(c)


c=oct(20)
print(c)

%%writefile ascii.py
a=chr(68)
b=chr(99)
print(id(a))
print(a,b)

%%writefile bitwise.py
#it halfs the nymber
a=1
k=bin(a)
print(k)
print(a>>1)

%%writefile shift.py
#it doubles the number
a=50
print(bin(a))
print(a<<1)

