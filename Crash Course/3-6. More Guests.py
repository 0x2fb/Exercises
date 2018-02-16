guest_list = ['Stephen Fry', 'Elon Musk', "Jim Carrey"]

print(f'I\'d invite {guest_list[0]} to dinner.')
print(f'I\'d also invite {guest_list[1]} to dinner.')
print(f'And I\'d invite {guest_list[2]} to dinner, too, of course.')

cancellation = 'Elon Musk'
guest_list.remove(cancellation)

print(f'Oh no, {cancellation} can\'t make it!')

guest_list.append('Jon Stewart')

print(f'I\'ll just invite {guest_list[2]} instead.' )
print(f'It\'ll be really exciting what he\'s going \
to ask {guest_list[0]} and {guest_list[1]} at the dinner.')
print()
print('I just found out that there\'s more room at the table than expected.')
guest_list.insert(0, 'Amy Poehler')
guest_list.insert(2, 'Joanna Newsom')
guest_list.append('Ellen Page')
print('I\'ll invite a few more people then.\n')
print('The final list includes:')
print(f'\t1. {guest_list[0]}\n\
\t2. {guest_list[1]}\n\
\t3. {guest_list[2]}\n\
\t4. {guest_list[3]}\n\
\t5. {guest_list[4]}\n\
\t6. {guest_list[5]}')