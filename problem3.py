#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

N=input('enter a user name: ')
if N == 'admin':
    P=input('enter password: ')
    if P == "12345password":
        print('Access granted')
    else:
        print('invalid password')
else:
    print('invalid user')

