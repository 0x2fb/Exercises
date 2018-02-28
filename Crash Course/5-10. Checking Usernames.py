current_users = ['helen', 'steve', 'amanda', 'laura', 'joseph', 'kyle']
new_users = ['Mary', 'JULES', 'theresa', 'steve']

for user in new_users:
    if user.lower() in current_users:
        print(f'{user} is already taken. Please pick a new username.')
    else:
        current_users.append(user.lower())
print(current_users)
