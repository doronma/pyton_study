ipAddress = input("Enter your IP Address :")
if ipAddress[-1] != '.':
    ipAddress+='.'


currentSegment = ''
for char in ipAddress:
    if char=='.':
        print(currentSegment)
        currentSegment=''
        continue 
    currentSegment+=char

# how to cut lines
print ("first line - "
       "second line")