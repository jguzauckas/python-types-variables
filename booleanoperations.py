#This program will demonstrate the basic operations that can be performed
#on booleans

#First, let's define two boolean variables
a = True
b = False

#Integer casting shows you the equivalent integer value of the boolean
print("\nInteger Casting:")
print("int("+str(a)+") =", int(a))
print("int("+str(b)+") =", int(b))

#The Not operation flips the value of a boolean to its opposite
print("\nNot:")
print("not", a, "=", not a)
print("not", b, "=", not b)

#The And operation combines two boolean values
#It outputs True if and only if both inputs are True, otherwise its false
print("\nAnd:")
print(a, "and", a, "=", a and a)
print(a, "and", b, "=", a and b)
print(b, "and", a, "=", b and a)
print(b, "and", b, "=", b and b)

#The or operation combines two boolean values
#It outputs False if and only if both inputs are False, otherwise its True
print("\nOr:")
print(a, "or", a, "=", a or a)
print(a, "or", b, "=", a or b)
print(b, "or", a, "=", b or a)
print(b, "or", b, "=", b or b)