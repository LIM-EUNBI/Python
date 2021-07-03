import menu as m

menu = m.Menu()

name = input("메뉴 : ")

while(name != ''):
    price = input("가격 : ")
    menu.getMenu(name, price)
    name = input("메뉴 : ")

menu.printList()