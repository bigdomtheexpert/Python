message=input("Please enter your message: ")
            ## this lets the user write down the message

key=int(input("Please enter the key: "))##here we adding the key to change the message

zero=("")##store a variable

for n in  range (0,len(message)): ##this is the length of the message
    
    numb=ord(message[n])
    numb=numb+key
    if numb>122: ##if the number is les than 122 it has to stop 
        numb=numb-26
    newletter=chr(numb)
    zero=zero+newletter

print(zero)##this will print it 
    
