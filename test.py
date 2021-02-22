print("pan duan run nian fan")
x = int(input("shu ru:")) #shu ru nian fen
y = x%4
z = x%100
q = x%400

if y == 0 :
    if z != 0 or q == 0:
        print ("shi yun nian")
    else:
        print ("bu shi yun nian")
else:
    print ("bu shi yun nian")
