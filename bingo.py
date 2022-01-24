import random

c = 0
while c <3:
    card = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
    r=0
    while r<3:
        i = 0
        while i<5 :
            if r == 1:
                card[r][i]=random.randint(31,60)
            elif r == 2:
                card[r][i]=random.randint(61,99)
            else:
                card[r][i]=random.randint(0,30)        
            i = i+1
        r = r+1    

    print("Card ", c+1)
    print("________________________")
    print("|",card[0][0],"|",card[0][1],"|",card[0][2],"|",card[0][3],"|",card[0][4])
    print("________________________")
    print("|",card[1][0],"|",card[1][1],"|",card[1][2],"|",card[1][3],"|",card[1][4])
    print("________________________")
    print("|",card[2][0],"|",card[2][1],"|",card[2][2],"|",card[2][3],"|",card[2][4])
    print("________________________")

    c = c+1