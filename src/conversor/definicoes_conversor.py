import os

class Conversor:
    """
    A converter class that converts numbers between binary and decimal formats.
    """

    def __init__(self, tipo_expressao, numero):
        """
        Initializes a new instance of the Conversor class.
        
        Args:
            tipo_expressao (str): The type of conversion ('binario' or 'decimal') indicating
                                  whether the given number is binary and should be converted
                                  to decimal, or vice versa.
            numero (int): The number to be converted.
        """
        self.tipo_expressao = tipo_expressao
        self.numero = numero

    def converter(self):
        """
        Converts the number from binary to decimal or from decimal to binary,
        depending on the tipo_expressao attribute. It then prints the result.
        """
        
        # Clear the console before showing the conversion result
        os.system('cls')

        # Convert from binary to decimal
        if self.tipo_expressao == 'binario':
            
            para_binario = 0
            for digito in str(self.numero):
                para_binario = para_binario * 2 + int(digito)
                
            print('O valor decimal de {} é {} \n'.format(self.numero, para_binario))

        # Convert from decimal to binary
        elif self.tipo_expressao == 'decimal':
            
            # For positive numbers or zero
            if self.numero >= 0:
                para_binario = bin(self.numero)[2:]  # Remove the '0b' prefix
                
            # For negative numbers, remove the '-0b' prefix
            elif self.numero < 0:
                para_binario = bin(self.numero)[3:]
                
            print('O valor binário de {} é {} \n'.format(self.numero, para_binario))
