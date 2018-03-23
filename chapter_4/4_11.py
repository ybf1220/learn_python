pizza = ['pizza A', 'pizza B', 'pizza C', 'pizza D']
friend_pizzas = pizza[:]
pizza.append('pizza E')
friend_pizzas.append('pizza F')
print('my favorite pizzas are:')
for p in pizza:
    print(p)
print('My friend’s favorite pizzas are:')
for fp in friend_pizzas:
    print(fp)