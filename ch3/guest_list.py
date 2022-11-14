guests = ['steve', 'elon', 'bill', 'obama']

message_steve = f'{guests[0].title()} you are gonna get a quality party like apple.'
message_elon = f"{guests[1].title()} if you can come in any car we wouldn't mind, but make sure you come."
message_bill = f"{guests[-2].title()} you can see our party arrangements on your microsoft, you wouldn't regret if you come."
message_obama =f"{guests[-1].title()} without you we can't start this party, Mr. President please come and enjoy!"

print(message_steve)
print(message_elon)
print(message_bill)
print(message_obama)

print(f'Sorry guests we got to know that Mr. {guests[-1].title()} could not come to the party.')

print("Here is the new guest list.")
guests.pop()
guests[-1] = 'kamala'

print(f"So don't worry in place of Mr. President Vice-President {guests[-1].title()} is coming.")

message_all = f"Guests {guests[0].title()}, {guests[1].title()}, {guests[2].title()} do not miss the opertunity to meet Vice-President."
print(message_all)

print("Hello guests now we have more famous personalities who are coming to the party.")

guests.insert(0, 'leonardo')
guests.insert(3, 'ronaldo')
guests.append('Lipa')
print(guests)

print(f"Guests {guests[0].title()}, {guests[3].title()}, {guests[-1].title()} are the new personalities who are coming to party.")

print("Sorry guests new guests can not make to the party on time, and we have only two places left at dinner table.")
print("We have to make hard choice we can't invite everyone.")

remove_guest = guests.pop()
print(f"{remove_guest.title()}, Sorry... we can't invite you to the party.")

remove_guest = guests.pop()
print(f"{remove_guest.title()}, Sorry... we can't invite you to the party.")

remove_guest = guests.pop()
print(f"{remove_guest.title()}, Sorry... we can't invite you to the party.")

remove_guest = guests.pop()
print(f"{remove_guest.title()}, Sorry... we can't invite you to the party.")


print(f"{guests[0].title()}, {guests[1].title()} you are still invited to the party!!")

del guests[0]
del guests[0]

print(guests)
