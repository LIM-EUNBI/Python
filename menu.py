class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []

    def getMenu(self, name, price):
        self.name = name
        self.price = price
        self.addMenu(name, price)
    
    def addMenu(self, name, price):
        self.menuList.append(name)
        self.priceList.append(price)

    def printList(self):
        for i in range(len(self.menuList)):
            print(self.menuList[i], self.priceList[i])

