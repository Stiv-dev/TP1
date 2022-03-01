def multiplication_egyptienne(a,b):
    i=0
    while a != 0:
        if(a%2) == 1:
            i = i+b
        b = b*2
        a = a//2
    return(i)

resultat=multiplication_egyptienne(13,23)
print(resultat)

    