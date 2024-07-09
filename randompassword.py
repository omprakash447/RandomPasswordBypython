import random
import string
x=string.ascii_uppercase
y=string.ascii_lowercase
z=string.punctuation
charval=string.ascii_lowercase + string.ascii_uppercase + string.punctuation
length=int(input("Enter the length of the password : "))
password=""
for i in range(length):
    password +=random.choice(charval)

print("Your password is : " , password)