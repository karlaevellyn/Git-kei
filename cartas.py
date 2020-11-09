print ("Olá, esse programa serve para te informar qual o número da quarta e última carta do mini-game. Lembrando que esses números estão entre 0 e 100, e que as quatro cartas formam dois pares de cartas iguais.")

a= int ( input ("Digite o número inteiro da primeira carta:"))
b= int ( input ("Digite o número inteiro da segunda carta:"))
c= int ( input ("Digite o número inteiro da terceira carta:"))

if ( a != b and a != c ):
    print (" O número da quarta carta é:", a)

elif ( a != b ) :
    print (" O número da quarta carta é: ", b)

else:
    print (" O número da quarta carta é: ", c)
    
