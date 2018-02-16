guest_list = ['Stephen Fry', 'Elon Musk', "Jim Carrey"]

print(f'The list contains {len(guest_list)} people.')

cancellation = 'Elon Musk'
guest_list.remove(cancellation)

print(f'The list contains {len(guest_list)} people.')

guest_list.append('Jon Stewart')

print(f'The list contains {len(guest_list)} people.')

guest_list.insert(0, 'Amy Poehler')
guest_list.insert(2, 'Joanna Newsom')
guest_list.append('Ellen Page')

print(f'The list contains {len(guest_list)} people.')