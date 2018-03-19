guests = ['Bill Gates', 'jobs', 'My Wife']
died = 'jobs'
new = 'Jack Chen'
guests.remove(died)
print("Sorry, " + died + " was died,can not arrive.")
guests.append(new)
for name in guests:
    message = 'Hi! ' + name + ',Do you have time for dinner?'
    print(message)
