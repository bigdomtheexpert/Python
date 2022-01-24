num=["1","2","3","4","5","6","7","8","9","10","11","12"]
for x in range (1, 13):
    for y in range (1, 13):
        print ('{:3}'.format(x*y), end=' ')
    print()
