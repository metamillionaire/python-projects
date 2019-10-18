# Check a user name and PIN code

database = [    ['albert',  '1234'],    ['dilbert', '4242'], ['jane doe','0456'] ,   ['smith',   '7524'],    ['jones',   '9843'] ]

username = input('User name: ')
pin = input('PIN code: ')

if [username, pin] in database: print('Access granted')
else:
    print('Invalid entry')
