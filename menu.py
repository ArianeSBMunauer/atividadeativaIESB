class Menu():
    def __init__(self):
        self.__opcao = None
    
    @staticmethod
    def apresenta_opcao():
        print("Bem vindo ao conversor de moedas da Ariane Câmbio!\n")
        print("Escolha abaixo a opção que deseja:\n")
        print('1 - Quero saber a cotação do dólar hoje')
        print('2 - Quero converter um valor de reais para euro')
        print('3 - Quero converter um valor de euro para dolar')
        print('4 - Sair\n')
        
        
    
    def valida_opcao(self, opcao):
        
        self.__opcao = opcao
        if (self.__opcao == 1 or self.__opcao == 2 or self.__opcao == 3 or self.__opcao == 4):
            return opcao
        else:
            print('Você digitou {}. Desculpe, mas opção escolhida é inválida. Vamos tentar novamente?\n'.format(opcao))
            opcao = input('Qual a opção desejada? ')
            self.valida_opcao(opcao)        
                   

   

        

