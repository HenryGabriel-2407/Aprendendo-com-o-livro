number = int(input("Digite qualquer número: "))
def collatiz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3 * number + 1

while number != 1:
    number = collatiz(number)
    print(number)