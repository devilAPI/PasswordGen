import random
import string
l = input("How long should your password be? My Answer: ")
n = int(l)
if n > 5000:
	print("Well... Thats a little too big for a password! Try a lower number!")
else:  
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    print("Your Password : " + str(res)) 
