cpf = [1,1,1,4,4,4,7,7,7]

Condição = False

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
