catName = []
print("Enter all your cat name one by one")
while True:
    print("Enter the " + str(len(catName)) + "th cat name of yours or to end (don't enter any thing)")
    name = input()
    catName = catName + [name]
    if name == '':
        break
print("the cat name are..")
for name in catName:
    print('' + name, end= "//")
    