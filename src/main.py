from conversor.definicoes_conversor import Conversor
import os

def verificar_tipo_numero(entrada: str):
    if all(digito in '01' for digito in entrada):
        return 'binario'
    else:
        return 'decimal'

def limpador(booleano):

    if (booleano):

        input('Precione ENTER para continuar...')

        # Verifica se o sistema operacional é Windows ou Unix-like
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')
    else:
        # Verifica se o sistema operacional é Windows ou Unix-like
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')

def main():

    os.system('cls')
    print('*********************************************************')
    print('****************** Bem-vindo ao Bin2Dec *****************')
    print('********************************************************* \n')
    limpador(True)

    while True:

        try:

            numero = input("Digite o valor numérico (até 8 dígitos): \n")
            if not numero.isdigit():
                raise ValueError

        except ValueError:

            limpador(False)
            print('Apenas valores numéricos são permitidos!! Tente novamente.\n')
            limpador(True)

        else:

            if (len(numero) <= 8):
                conversor = Conversor(verificar_tipo_numero(numero), int(numero))
                conversor.converter()
                break
            else:

                limpador(False)
                print('Digite um valor com 8 ou menos dígitos!! \n')
                limpador(True)

    limpador(True)

if __name__ == "__main__":
    main()
