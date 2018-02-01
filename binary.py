for i in range(33):
    print ("{0:>2} in binary is {0:>08b} in hex its {0:>2x}".format(i))

binA = 0b100
hexA = 0x1d
print (binA)  
print (hexA) 
result = ''; 

decNum = input("Add input dec: ")
power = 1
while (power<decNum):
    power*=2
power = power/2    

