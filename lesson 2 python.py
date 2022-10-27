#factorial
fac = int(input('Please enter a number:'))
factorial = 1
if fac < 0: 
    print("Sorry, factorial does not exist for negative numbers")
elif fac == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,fac + 1):
       factorial = factorial*i
   print("The factorial of",fac,"is",factorial)

   
#doubleIt
  str = input("please enter a phrase that you would like to 'double':")

res = ""
for i in range(len(str)):
    res = res + str[i] +str[i]
print(res)


#camelCase
name = input("Please enter a file name")
name = name.lower()
name = name.title()
name = name[0].lower() + name[1:]
name = name.replace(" ", "")
name = name.replace("/", "-")
print(name)


   
