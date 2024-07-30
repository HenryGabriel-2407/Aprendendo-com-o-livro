pessoas = []
a = True
while a:
    print("+="*30)
    input_nome = input("Digite o nome: ")
    input_genero = input("[M/F]: ")
    input_idade = int(input("Digite a idade: "))
    input_continuar = input("Quer continuar? [S/N]: ")
    if input_continuar.lower() == 'n':
        a = False

    pessoa = {'nome': input_nome, 'gênero': input_genero.lower(), 'idade': input_idade}
    pessoas.append(pessoa)

def listar_acima_media(media):
    print("Pessoas com idade acima da média")
    for i in range(len(pessoas)):
        if pessoas[i]['idade'] > media:
            print(f"Nome: {pessoas[i]['nome']} | Gênero: {pessoas[i]['gênero']} | Idade: {pessoas[i]['idade']}")

def calcular_media():
    idade = 0
    for i in range(len(pessoas)):
        idade+= pessoas[i]['idade']
    media = idade / len(pessoas)
    print(f"\nA idade média das pessoas cadastrada é de {media} anos.")
    listar_acima_media(media)

def listar_mulheres():
    print("Mulheres cadastrada: \n\t", end='')
    for i in range(len(pessoas)):
        if pessoas[i]['gênero'] == 'f':
            print(f"{pessoas[i]['nome']}", end=' ')

print(f"A quantidade de pessoas registradaas é de {len(pessoas)}")
listar_mulheres()
calcular_media()