cpf = [1,1,1,4,4,4,7,7,7]

Condição = False
Condição2 = False

while Condição != True:
    contador = 10
    Multiplicados = []
    for i in cpf:
        resultado = i * contador
        Multiplicados.append(resultado)
        contador -= 1
        if contador == 1:
            print(Multiplicados)
            Condição = True

Divisão = sum(Multiplicados)/11
print(Divisão)
Resto = sum(Multiplicados)%11 
print(Resto)

def verificacao1(Valor):
    if Resto < 2:
        Dígito = 0       
    if Resto >= 2:
        Dígito = 11 - Resto       
    return Dígito

print(verificacao1(Resto))
cpf.append(verificacao1(Resto))

while Condição2 != True:
    contador2 = 11
    Multiplicados2 = []
    for i in cpf:
        resultado2 = i * contador2
        Multiplicados2.append(resultado2)
        contador2 -= 1
        if contador2 == 1:
            print(Multiplicados2)
            Condição2 = True

Divisão2 = sum(Multiplicados2)/11
print(Divisão2)
Resto2 = sum(Multiplicados2)%11 
print(Resto2)

def verificacao2(Valor2):
    if Resto2 < 2:
        Dígito2 = 0       
    if Resto2 >= 2:
        Dígito2 = 11 - Resto2       
    return Dígito2

cpf.append(verificacao2(Resto2))
print(cpf)