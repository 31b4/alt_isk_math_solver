kilepes = False
while kilepes != True:
    a = int(input("a ="))
    b = int(input("b ="))
    k = (a+b)*2
    t = a*b
    print("Terület:",t)
    print("Kerület:",k)
    if a == b :
        print("Ez egy négyzet!!")
    else :
        print("Ez egy téglalap")
    i = input("Kilépsz???q ")
    if i == "q":
        kilepes = True

    
