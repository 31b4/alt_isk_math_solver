kilepes = False
while kilepes != True:
    a = str(input("Kérem a jelszót! :"))
    b = "0000"
    c = "jelszo"
    if a == b or a == c:
        a = int(input("szám = "))
        i=1
        while i<a:
            i=i+1
            if a%i==0:
                a=a/i
                print(i)
                i=1
    else :
         print("TÉVES A JELSZÓ")
    i = input("HA KI AKARSZ LÉPNI NYOMD MEG A q-T ÉS EGY ENTER-T ")
    if i == "q":
        kilepes = True

                             


  
        
