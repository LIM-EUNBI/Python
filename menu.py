class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []
        f = open("d:/tmp/menu.txt", "r")
        while True:
            lst = f.readline()
            if lst == "":
                break
            lst = lst.split(',')
            name = lst[0].strip()
            price = lst[1].strip()
            self.addMenu(name, price)
        f.close()
    #with open(경로) as file:
    #   for line in file:
    #       name, price = line.split(",")
    #       price = price[0: len(price) -1]
    #       self.menulist.append(name)
    #       slef.pricelist.append(price)
    #       for i in range(len(menulist)):
    #           print(self.menulist[i], self.pricelist[i])


    def addMenu(self, name, price):
        self.menuList.append(name)
        self.priceList.append(price)

    def printList(self):
        for i in range(len(self.menuList)):
            print(self.menuList[i] + ", " + self.priceList[i])

    def saveList(self):
        # menu.txt 파일을 연다. w, for문 실행 menu, 가격
        f = open("d:/tmp/menu.txt", "w")
        for i in range(len(self.menuList)):
            f.write(self.menuList[i] + ", " + self.priceList[i] + "\n")
        f.close()

    def readList(self):
        f = open("d:/tmp/menu.txt", "r")
        fl = f.read()
        print(fl)