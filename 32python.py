def add(a,b):
    return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return a*b

def divide(a,b):
	return a/b

i=int(input("enter value of a:"))
i=int(input("enter value of b:"))
o=input("what do you want to do? +,-,*,/")

if(o=='+'):
	res=add(i,j)
elif(o=='-'):
	res=sub(i,j)
elif(o=='X'):
	res=mult(i,j)
elif(o=='/'):
	res=divide(i,j)

print(res)