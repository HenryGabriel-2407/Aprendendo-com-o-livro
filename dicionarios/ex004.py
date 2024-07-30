from random import randint

jogadores = {'jogador0': 0, 'jogador1': 0, 'jogador2':0, 'jogadore3': 0}

for i in jogadores.keys():
    jogadores[i] = randint(0, 20)

print("Ordem dos jogadores: ")
for k, v in jogadores.items():
    print(f"\tO {k}: {v}")

dict_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print("RANKING:")
for k, v in dict_ordenado.items():
    print(f"\tO {k}: {v}")