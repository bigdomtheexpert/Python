again = "yes"
while again == "yes":


    num = int(input("choose a number "))
    numb = int(input("choose another number "))
    symbol = input("choose one (+  -  *  /)")

    if symbol =="+":
        print("your answer is ",num+numb)
    elif symbol =="-":
        print("your answer is ",num-numb)
    elif symbol =="*":
        print("your answer is ",num*numb)
    elif symbol =="/":
        print("your answer is ",num/numb)
    else:
        print("that was not an option")
    again = input("\ndo you want to try again (yes or no) ").lower()

        
