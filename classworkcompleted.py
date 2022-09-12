#This Python file needs to be completed so that the output matches what is written
#in classwork.txt

#Here is a sample:
a = 5
b = 10
print(a + b) #Note that this just prints the sum, that's okay!

#First, define variables with the values 16, 35, 13.2, 23.6, True, False, "Hello", "World"
a = 16
b = 35
c = 13.2
d = 23.6
e = True
f = False
g = "Hello"
h = "World"

#Next lets do some operations. Using print, your variables, and your operations, do
#16 + 35, 35 - 13.2, 13.2 * 23.6, 23.6 / 16, 35 // 16, 16 ** 13.2
print(a + b)
print(b - c)
print (c * d)
print(d / e)
print(b // a)
print(d % a)
print(a ** c)

#not True, True and False, True or False
print(not e)
print(a and b)
print(a or b)

#The length of "Hello", the third character of "World", from beginning to position 4 of "Hello"
#from position 2 to end of "World", from position 2 to position 5 of "Hello"
print(len(g))
print(h[2])
print(g[:4])
print(h[2:])
print(g[2:5])