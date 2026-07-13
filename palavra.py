palavra_secreta = 'teste'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:  
      print('Digite apenas uma letra.')
      continue
    
    if letra_digitada in palavra_secreta:
       letras_acertadas += letra_digitada

    print(letras_acertadas)  
