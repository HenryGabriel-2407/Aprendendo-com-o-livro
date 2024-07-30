myCat = {'nome': 'Beraldo', 'cor': 'cinza', 'tamanho':'pequeno', 1245: 'xique-xique'}
print(f"{myCat['cor']}, {myCat[1245]}")
print(f"{myCat.keys()}")

# ----------------------------------------
aniversario = {'Alice': '11 de dezembro', 'Bob': '14 de abril', 'Mario': '19 de junho'}
while True:
    
    input_nome = str(input("Digite o nome a ser pesquisado:"))

    if input_nome == '':
        break
    if input_nome in aniversario:
        print(f"O aniversário de {input_nome} é no dia {aniversario[input_nome]}")
    else:
        print(f"{input_nome} não está no banco de dados")
        novo_ani = input("Digite o aniversário da pessoa: ")
        aniversario[input_nome] = novo_ani
        print("Banco de dados atualizado!!\n")