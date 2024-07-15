import random 
# enter the lowercase ,uppercase,numbers,and symbols 
chars ="abcdefghijklmnopqrstuvwcyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#_*()[]{}"
# enter the length
length = int(input("Enter length : " ))
password = "  "
for a in range(length):
	password += random.choice(chars)
	print(password)
