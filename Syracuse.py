def syracuse(U):
    while U != 1:
        if U%2 == 0 :
            U = U // 2
        else :
            U = U*3 + 1
        print(U)
U = int(input("Veuillez entrer le premier terme :"))
print(U)
syracuse(U)