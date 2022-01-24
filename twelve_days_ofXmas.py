gifts=[
"Three French hens",
"Two turtle-doves",
"partridge in a pear tree"]
gifts_len = len(gifts)
days=["first","second","third","fourth","fith",
"sixth",]
for i in range(0,gifts_len):
    print("On the",days[i],"day of Christmas")
    print("My true love sent to me")
    for n in range(gifts_len-1-i,gifts_len):
        print(gifts[n])
    print("")