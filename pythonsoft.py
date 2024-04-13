print ("create an account")

username = input(' create a username')
password = input(' create a password')
email = input(' create a email')
print ("account successfuly created")


print ('please login')
username2 = input(' create a username2')
password2 = input(' create a password2')
email2 = input(' create a email2')


if username == username2 and password == password2:
    print ("Login Passed")
else:
    print ("Login failed")