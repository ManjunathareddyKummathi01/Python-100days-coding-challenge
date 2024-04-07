%%writefile list5.py
#mutable
#ordered
#duplicates allowed
fruits=["mango","apple","banana","grapes"]
print(len(fruits))
print(dir(fruits))
print(help(fruits))
print(fruits.append("pineapple"))
print(fruits.pop())
print(fruits.remove("banana"))
print(fruits.insert(1,"pomogranate"))
print(fruits.sort())
print(fruits.reverse())
print(fruits.index("grapes"))
print(fruits.count("mango"))
print(fruits.copy())
print(fruits.clear())


%%writefile tuple1.py
#ordered,immutable,duplicates allowed
ann=("manju","manasa","nagesh","vanitha",1,18)
print(len(ann))
print(dir(ann))
print(help(ann))
print(ann.index("vanitha"))
print(ann.count("manasa"))




%%writefile llpp.py
#conversion of tuple into list.........😎
man=[("manju","manasa","kk","sravani","sarala","bhavya")]
print(type(man))
