class ShoppingList:
    def __init__(self):
        self.list = {}

    def add_to_list(self, purchase: str):
        if self.__check_in_list(purchase):
            self.list[purchase] += 1
        else:
            self.list[purchase] = 1

    def print_list(self):
        print('----------------------------------------')
        for purchase, value in self.list.items():
            print("{0}: {1}".format(purchase, value))
        print('----------------------------------------')

    def __check_in_list(self, value: str):
        for i in self.list:
            if i == value:
                return True
        return False


def main():
    shopping_list = ShoppingList()
    while True:
        purchase = input("Add purchase: ")
        if not purchase:
            break

        shopping_list.add_to_list(purchase)
    shopping_list.print_list()



if __name__ == '__main__':
    main()