input_nome = input("Digite o nome do aluno: ")
input_media = float(input(f"Digite a média do(a) {input_nome}: "))
dicionario = {'nome': input_nome, 'média': input_media}

print(f"O nome é {dicionario['nome']}")
print(f"A média é {dicionario['média']}")
if dicionario['média'] >= 7:
    print("A situação é aprovada!")
else:
    print("A situação é reprovada!")