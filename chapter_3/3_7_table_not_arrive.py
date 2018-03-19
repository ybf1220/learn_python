guests = ['Bill Gates', 'jobs', 'My Wife']
died = 'jobs'
new = 'Jack Chen'
guests.remove(died)
print("Sorry, " + died + " was died,can not arrive.")
guests.append(new)
for name in guests:
    message = 'Hi! ' + name + ',Do you have time for dinner?'
    print(message)
print("there ia a bigger table，can allow more people.")
more_guest = ['A', 'B', 'C']
guests.insert(0, more_guest[0])
guests.insert(2, more_guest[1])
guests.append(more_guest[2])
for name in guests:
    message = 'Hi! ' + name + ',Do you have time for dinner?'
    print(message)
print("Sorry Again,the table can not be arrived.")
deleted_num = len(guests) - 2
for i in range(deleted_num):
    name = guests.pop()
    print('Sorry, ' + name + ', I can not have dinner for you')
for name in guests:
    message = 'Hi! ' + name + ',Do you have time for dinner?'
    print(message)


