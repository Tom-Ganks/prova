menor_altura = float("inf")
maior_altura =  float("-inf")

for inf in range(1, 16):
    height = float(input("Digite a altura da pessoa {inf}}: "))

    if height < menor_altura:
        menor_altura = height

    if height > maior_altura:
        maior_altura = height

        print(f"A maior altura é {maior_altura} metros")
        print(f"A menor altura é {menor_altura} metros")