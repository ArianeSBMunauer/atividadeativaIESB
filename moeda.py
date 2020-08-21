import json as j
import requests as r

class Moeda():
    def __init__(self):
        self.__dolar
        self.__euro
        self.__real
    
    @property
    def dolar(self):
        self.__dolar = 0
        return self.__dolar
    
    @property
    def euro(self):
        self.__euro = 0 
        return self._euro
    
    @real.setter 
    def real(self, valor):
        self.__real = valor
    
    

