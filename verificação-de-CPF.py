cpf = []
cpfVerificacao = []

while len(cpf) <= 10:
    Algarismos = int(input("Escreva um dígito do seu cpf de cada vez: "))
    if len(str(Algarismos)) > 1:
        print("Nao pode escrever esse numero.")
    else:
        cpf.append(Algarismos)
        cpfVerificacao.append(Algarismos)

cpf.pop()
cpf.pop()

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
            Condição = True

Divisão = sum(Multiplicados)/11
Resto = sum(Multiplicados)%11 

def verificacao1(Valor):
    if Resto < 2:
        Dígito = 0       
    if Resto >= 2:
        Dígito = 11 - Resto       
    return Dígito

cpf.append(verificacao1(Resto))

while Condição2 != True:
    contador2 = 11
    Multiplicados2 = []
    for i in cpf:
        resultado2 = i * contador2
        Multiplicados2.append(resultado2)
        contador2 -= 1
        if contador2 == 1:
            Condição2 = True

Divisão2 = sum(Multiplicados2)/11
Resto2 = sum(Multiplicados2)%11 

def verificacao2(Valor2):
    if Resto2 < 2:
        Dígito2 = 0       
    if Resto2 >= 2:
        Dígito2 = 11 - Resto2       
    return Dígito2

cpf.append(verificacao2(Resto2))

if cpf == cpfVerificacao:
    print("CPF Válido")
else:
    print("CPF Inválido")