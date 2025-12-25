birthdays = {'Alice':'april 1', 'bob':'dec 12','carol':'march 4'}
while True:
    print('enter your name,(keep blank to leave)')
    name = input()
    if name == '' :
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        if name not in birthdays:
            print('I do not have birthday information for ' + name + "What is their birthday?")
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')
