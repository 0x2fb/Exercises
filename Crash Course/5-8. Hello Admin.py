usernames = ['helen', 'steve', 'amanda', 'laura', 'joseph', 'admin']

for user in usernames:
    print(f'Welcome back, {user.title()}.')
    if user == 'admin':
        print('Would you like to see a status report?')
