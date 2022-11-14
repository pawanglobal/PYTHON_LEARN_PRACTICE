friends =['john', 'steve', 'pawan', 'veena', 'harmesh']
print(friends[0].title())
print(friends[1].title())
print(friends[-1].title())
print(friends[-2].title())

message = f"\nHey! {friends[-1].title()} you are a good man."
print(message)

favorite_transportations = ['cycle', 'bus', 'taxi', 'train']

message_cycle = f'\nI love to go near places by {favorite_transportations[0]}.'
message_bus = f'\nIn public transport I would love to go by {favorite_transportations[1]}.\n'

print(message_cycle)
print(message_bus)