def palindromo(num: int):
    invertido = 0
    original = num

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num = num // 10

    if original == invertido:
        return True
    else:
        return False


def main():
    num = int(input('Digite um número entre 1 e 10000: '))

    while num <= 1 or num >= 10000:
        num = int(input('Número inválido! Digite novamente: '))

    if palindromo(num):
        print('O número já é palíndromo!')
    else:
        proximo = num + 1
        encontrado = False

        while encontrado == False:
            if palindromo(proximo):
                encontrado = True
            else:
                proximo = proximo + 1

        print('O próximo palíndromo é:', proximo)


if __name__ == '__main__':
    main()