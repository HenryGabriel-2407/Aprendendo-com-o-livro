from random import randint

quantidade_partidas = []
total_gols = 0
input_nome = input("Digite o nome do jogador: ")
quantidade = int(input("Digite a quantidade de partidas: "))

for i in range(quantidade):
    gols = randint(0, 4)
    quantidade_partidas.append(gols)
    total_gols+= gols

jogador = {'nome': input_nome, 'gols_partidas': quantidade_partidas, 'total_gols': total_gols}
print("+="*30)
print(jogador)
print("+="*30)

for k, v in jogador.items():
    print(f"No campo {k} o valor é {v}")

print("+="*30)
print(f"O jogador {input_nome} em {quantidade} partidas:")

for i in range(len(jogador["gols_partidas"])):
    print(f"\t Partida {i+1}: {jogador['gols_partidas'][i]} gols")
print(f"O {list(jogador.keys())[2]} é {list(jogador.values())[2]}")