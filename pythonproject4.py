import random 
chars ="abcdefghijklmnopqrstuvwcyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#_*()[]{}"
length = int(input("Enter length : " ))
password = "  "
for a in range(length):
	password += random.choice(chars)
	print(password)