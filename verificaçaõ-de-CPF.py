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


valor1 = sum(Multiplicados)/11
print(valor1)
valor2 = sum(Multiplicados)%11 
print(valor2)