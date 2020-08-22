from menu import Menu
from moeda import Moeda

#cria o objeto menu
menu = Menu()

#faz a abertura do programa de forma amigável para o usuário
Menu.apresenta_opcao()
opcao = input("Escreva o número de sua escolha e aperte enter em seguida: ")
opcao = int(opcao)

#valida a opção escolhida pelo usuário
menu.valida_opcao(opcao)


#apresenta a opção escolhida e 
moeda = Moeda(opcao)
moeda.cambio()


