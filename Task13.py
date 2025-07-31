pwd = input('Enter password')

if len(pwd) >= 8 and any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd):
    print('Strong Password')
else:
    print('Weak Password')    