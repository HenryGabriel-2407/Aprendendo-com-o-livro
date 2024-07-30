"""def hello(nome):
    print(f"Olá, {nome}!")
    return f"Seu nome tem {len(nome)} letras!"

print(hello("Henry"))
print(hello("Alessandra"))"""

"""spam = print('Hello')
print(None == spam)"""

"""print("Papagaio", "Girafa", "Raposa")
print("Papagaio", "Girafa", "Raposa", sep=';')"""

"""def spam():
    eggs = 203
spam()"""
#print(eggs)  = error

"""def bacon():
    ham = 101
    eggs = 92

def spam():
    eggs = 99
    bacon()
    print(eggs)

spam()"""

"""def spam():
    print(eggs) #acessar variáveis globais

eggs = 23
spam()
print(eggs)"""

"""def spam():
    global eggs #acessa e modifica uma variável global
    eggs = 0

eggs = 100
spam()
print(eggs)"""

def spam(num):
    try:
        return 120/num
    except ZeroDivisionError:
        return "Erro divisão por zero."

print(spam(2))
print(spam(5))
print(spam(0))
print(spam(10))