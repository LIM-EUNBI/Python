import menu as m

menu = m.Menu()

name = input("메뉴 : ")

while(name != ''):
    price = input("가격 : ")
    menu.addMenu(name, price)
    name = input("메뉴 : ")


menu.printList()
menu.saveList()