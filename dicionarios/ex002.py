filme = {'título': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}
print(filme.keys())
print(filme.values())
print(filme.items())
print()

for k, v in filme.items():
    print(f"O {k} do filme é {v}")
print()

locadora = []
def listar():
    print("A lista do filme: ")
    for i in range(len(locadora)):
        print(f"O título é {locadora[i]['título']}")
        print(f"O ano é {locadora[i]['ano']}")
        print(f"O diretor é {locadora[i]['diretor']}")
        print()

while True:
    input_titulo = input("Digite o título do filme (digite nada se terminar): ")
    if input_titulo =='':
        listar()
        break
    input_ano = int(input("Digite o ano de lançamento: "))
    input_diretor = input("Digite o nome do diretor(a): ")
    filme = {'título': input_titulo, 'ano': input_ano, 'diretor': input_diretor}
    locadora.append(filme)
    print()