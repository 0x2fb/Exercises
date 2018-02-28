# usernames = ['helen', 'steve', 'amanda', 'laura', 'joseph', 'admin']
usernames = []

if usernames:
    for user in usernames:
        print(f'Welcome back, {user.title()}.')
        if user == 'admin':
            print('Would you like to see a status report?')
else:
    print('There are no users in the database.')
