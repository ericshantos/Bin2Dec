from conversor.definicoes_conversor import Conversor
import os

def verificar_tipo_numero(entrada: str):
    """
    Determines if the input string represents a binary or decimal number.
    
    Args:
        entrada (str): The input string to be checked.
        
    Returns:
        str: 'binario' if the input is binary, 'decimal' otherwise.
    """
    # Check if every character in the input string is either '0' or '1'
    if all(digito in '01' for digito in entrada):
        return 'binario'
    else:
        return 'decimal'

def limpador(booleano):
    """
    Clears the console screen. If the input boolean is True, it waits for the user
    to press ENTER before clearing the screen.
    
    Args:
        booleano (bool): Determines the behavior for waiting on user input.
    """
    if booleano:
        input('Pressione ENTER para continuar...')
    
    # Execute the command to clear the screen based on the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def main():
    """
    Main function that runs a loop to accept numeric input from the user,
    determines its type (binary or decimal), and converts it accordingly.
    """
    # Clear the screen at the start of the program
    os.system('cls')
    print('*********************************************************')
    print('****************** Welcome to Bin2Dec *******************')
    print('********************************************************* \n')
    limpador(True)

    while True:
        try:
            numero = input("Insira o valor numérico (até 8 dígitos): \n")
            # Check if the input is purely numeric
            if not numero.isdigit():
                raise ValueError

        except ValueError:
            # Handle non-numeric input
            limpador(False)
            print('Somente valores numéricos são permitidos!! Por favor, tente novamente.\n')
            limpador(True)

        else:
            # Proceed if the input length is 8 or fewer digits
            if len(numero) <= 8:
                conversor = Conversor(verificar_tipo_numero(numero), int(numero))
                conversor.converter()
                break
            else:
                # Handle input longer than 8 digits
                limpador(False)
                print('Por favor, insira um valor de 8 ou menos dígitos!! \n')
                limpador(True)

    # Clear the screen before ending the program
    limpador(True)

if __name__ == "__main__":
    main()

