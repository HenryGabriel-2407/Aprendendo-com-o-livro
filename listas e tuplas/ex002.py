#Código para vírgulas
#Suponha que você tenha um valor de lista como: spam = ['apples', 'bananas', 'tofu', 'cats']
#Crie uma função que aceite um valor de lista como argumento e retorne uma string com todos os itens separados por uma vírgula e um espaço, com and inserido antes do último item. Por exemplo, se passarmos a lista spam anterior à função, 'apples, bananas, tofu, and cats' será retornado. Porém sua função deverá ser capaz de trabalhar com qualquer valor de lista que ela receber.

spam = ['apples', 'bananas', 'tofu', 'cats']
frase = ''

for palavra in range(len(spam) - 1):
    if palavra == (len(spam) -2):
        frase += f"{spam[palavra]} "
    else:
        frase += f"{spam[palavra]}, "

frase += f"and {spam[-1]}"

print(frase)