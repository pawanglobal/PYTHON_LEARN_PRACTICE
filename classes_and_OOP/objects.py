#string object and manuplation
message = "hello world"
message = message.upper()

print(message)

#replace method
new_message = message.replace("HELLO WORLD", "Hello My World")

print(new_message)

#split method to convert them into lists
new_msg_lst = new_message.split()

print(new_msg_lst)

#list object
names = ['paul', 'marx', 'einstein']
names.append('messy') #to add new object

print(names)

names[1] = 'you'      #to add new object

print(names)

#to check associate type of a object
print(type(names))