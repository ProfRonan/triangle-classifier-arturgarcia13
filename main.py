ladoA = int(input("Digite a medida do lado A: "))
ladoB = int(input("Digite a medida do lado B: "))
ladoC = int(input("Digite a medida do lado C: "))

testeTri = ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA

triEqui = ladoA == ladoB and ladoB == ladoC
triIsos = ladoA == ladoB and ladoB != ladoC
triEsc = ladoA != ladoB and ladoB != ladoC and ladoC != ladoA

if testeTri is True :
    if triEqui is True :
        print('Equilátero')
    elif triIsos is True :
        print('Isósceles')
    elif triEsc is True :
        print('Escaleno')

else:
    print("Não é um triângulo")