def picnictable(Itemdict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth +rightwidth, '-'))
    for k, v in Itemdict.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))
picnicItems = {'cup':10, 'plate':5, 'matchstick':1, 'trolly':1}
picnictable(picnicItems, 15, 5)