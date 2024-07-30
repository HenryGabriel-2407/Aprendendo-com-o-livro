# [] --> uma lista
#Como você atribuiria o valor 'hello' como o terceiro valor de uma lista armazenada em uma variável chamada spam? (Suponha que spam contenha [2, 4, 6, 8, 10].)
spam = [2, 4, 6, 8, 10]
spam.insert(2, 'hello')
print(f"{spam}\n")

lista = ['a', 'b', 'c', 'd']
# TypeError --> spam[int(int('3' * 2) / 11)]

# Para que valor spam[-1] é avaliado? 'd'
print(f"{lista[-1]}")

#Para que valor spam[:2] é avaliado? --> 'a', 'b'
print(f"{lista[:2]}")

bacon = [3.14,'cat', 11, 'cat', True]
# 6. Para que valor bacon.index('cat') é avaliado? --> 1
print(f"{bacon.index('cat')}\n")
# 7. Como bacon.append(99) altera o valor de lista em bacon? --> colocando 99 no último item da lista
bacon.append(99)
print(f"{bacon}")
# 8. Como bacon.remove('cat') altera o valor de lista em bacon?  --> removerá o item na sua primeira ocorrência
bacon.remove('cat')
print(f"{bacon}")

#9. Quais são os operadores para concatenação de lista e para repetição de lista? --> += e *=
#10. Qual é a diferença entre os métodos de lista append() e insert()? --> append() adiciona o item na última posição, e insert() adiciona o item na posição que 'quiser'
#11. Quais são as duas maneiras de remover valores de uma lista? --> remove() e pop()
#12. Nomeie alguns aspectos em relação aos quais os valores de lista são semelhantes aos valores de string. -->  string é uma lista de caracteres, lista e string possuem os mesmos 'tratamentos'
#13. Qual é a diferença entre listas e tuplas? --> lista são mutáveis e usa-se [], já as tuplas são imútaveis e usa-se ()
#14. Como você deve digitar o valor de uma tupla que contenha somente o valor inteiro 42? --> nome_da_tupla[posição]
#15. Como podemos obter a forma de tupla de um valor de lista? Como podemos obter a forma de lista de um valor de tupla? --> tuple(lista) e list(tupla)
#16. As variáveis que “contêm” valores de lista não contêm realmente as listas diretamente. O que elas contêm em seu lugar?  --> referências
#17. Qual é a diferença entre copy.copy() e copy.deepcopy()? -->  copy.copy() vai copiar uma lista, e copy.deepcopy() vai copiar listas internas de uma lista