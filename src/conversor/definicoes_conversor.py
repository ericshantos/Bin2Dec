import os

class Conversor:

    def __init__(self, tipo_expressao, numero):

        self.tipo_expressao = tipo_expressao
        self.numero = numero

    def converter(self):
        os.system('cls')

        if (self.tipo_expressao == 'binario'):

            para_binario = 0
            for digito in str(self.numero):

                para_binario = para_binario * 2 + int(digito)

            print('O valor decimal de {} é {} \n'.format(self.numero, para_binario))

        elif (self.tipo_expressao == 'decimal'):

            if (self.numero >= 0):

                para_binario = bin(self.numero)[2:]

            elif (self.numero <= 0):

                para_binario = bin(self.numero)[3:]

            print('O valor binário de {} é {} \n'.format(self.numero, para_binario))