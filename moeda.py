import json 
import requests



class Moeda():
    def __init__(self, opcao):
        self.__opcao = opcao
        self.__r = None
   

    def consulta_api(self):
        response = requests.get('http://economia.awesomeapi.com.br/json/all')
        self.__r = response.json()
        return self.__r


    def cambio(self):     

        if(self.__opcao == 1):
            r = self.consulta_api()
            r = r['USD']['ask']
            print('A cotação do dolar hoje é R${}'.format(r))

        elif(self.__opcao == 2):
            valor_real = input('Por favor, informe o valor que deseja converter em reais: R$ ')
            valor_real = str(valor_real).replace(',','.')
            valor_real = float(valor_real)
            r = self.consulta_api()
            r = r['EUR']['ask']
            conversao = valor_real * float(r)
            valor_real = str(valor_real).replace('.',',')
            conversao = str(conversao).replace('.',',')
            print('O valor de R${}0 corresponde a {} €.\n\n'. format(valor_real, conversao))

        elif(self.__opcao == 3):
            pass
