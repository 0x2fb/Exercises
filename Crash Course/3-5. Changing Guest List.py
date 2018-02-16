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