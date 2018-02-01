number = "123,456,789"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print (number[i])

cleanNumber = ''
for char in number:
    if char in '0123456789':
        #Augmented Assignment is much better
        cleanNumber += char
newNumber = int(cleanNumber)
print("New Number is {}".format(newNumber))

for state in ["state1","state2","state3"]:
    print("The state is - " + state)

# using steps
for i in range(10,60,10):
    print("i is - {}".format(i))

# continue & break
shopping_list = ["milk","pasta","eggs","spam","bread","rice","stam1","stam2"]
for item in shopping_list:
    if (item == 'spam'):
        continue
    if (item=='stam1'):
        break
    print("Item is - {}".format(item))
else :
    print("the loop finished without a break....")

num = 3
num *=3
print (num)

message = "Hello World! "
message *=2
print(message)


