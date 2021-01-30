vendedor = input("Olá caro colaborador tudo bem, como voce se chama?")
produto1 = float(input("Insira o valor do produto 1: "))
produto2 = float(input("Insira o valor do produto 2: "))
produto3 = float(input("Insira o valor do produto 3: "))

soma = produto1+produto2+produto3
print(f"{vendedor}, A soma das vendas dos produtos é {soma}")

if soma >= 1000:
    total= soma * 0.05
    print(f"O valor do seu agrado mensal será de de 5% no valor de {total}")
else:
    total= soma* 0.07
    print(f"O valor do seu agrado mensal será de 7% no valor de {total}")
