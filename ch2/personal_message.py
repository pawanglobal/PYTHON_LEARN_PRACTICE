person_name = "Pawan"

message = f"\nHey! {person_name.upper()} would you like to learn Python today."
print(message)

print(person_name.upper())
print(person_name.lower())
print(person_name.title())

person = "albert einstein"
quote =f'\n{person.title()} once said, " A person who never made a mistake never tried anything new."'
print(quote)

famous_person =f"{person}"
message = f'\n{famous_person.title()} once said, " A person who never made a mistake never tried anything new."'
print(message)

name ='         pawan '
print(name)
print("\nRemoving whitespaces:")
print("\n",name.strip())
print("\n",name.rstrip())
print("\n",name.lstrip())
