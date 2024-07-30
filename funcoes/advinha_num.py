from random import randint

num = randint(1, 20)

def verificador(input_num, tentaivas):
    if input_num == num:
        print(f"Este é o número! Você conseguiu em {tentativas} tentaiva(s)!")
        return True
    elif input_num > num:
        print("É um número mais baixo")
        return False
    elif input_num < num:
        print("É um número mais alto")
        return False
    
tentativas = 0 
while verificador != True:
    try:
        input_num = int(input("Digite um número entre 1 a 20: "))
        tentativas += 1
        if verificador(input_num, tentativas) == True:
            break
    except:
        print("Valor inválido")