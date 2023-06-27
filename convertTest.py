# input
num1 = input("Give me an integer.")
num2 = input("Give me another integer.")

# first print
print("You just gave me two numbers.")
print("When I am given input, it turns it into a string.")
print("For example, if I try to add these two integers:")
print(num1)
print(num2)
print("They will be appended to one another as strings.")
print("Like so:")
print(num1,"+",num2,"=",num1 + num2)
print("However, I can convert them into integers.")

# conversion
num1 = int(num1)
num2 = int(num2)

#second print
print("Now, you see them as",num1,"and",num2,".")
print("And when I add them together, you should get a different result.")
print("Like so:")
print(num1 + num2)
