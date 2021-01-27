print("Hello World")

name = input('What is your name?\n')
print ('Hi, %s.' % name)


friends = ['First', 'Second', 'Third', 'Fourth']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))


    def greet(name):
        print ('Hello', name)

greet('Gabe')
greet('Jill')
greet('Bob')