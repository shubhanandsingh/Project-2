def isvalidnumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for j in range(4, 7):
        if not text[j].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    else:
        return True
print('the number 334-345-7545 is :')
print(isvalidnumber('334-345-7545'))
message = 'hello i will be back at 748-860-3968 after 9pm, and at 700-473-2461 after 6 am'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isvalidnumber(chunk):
        print('the number is: ' + chunk)
print('Done')