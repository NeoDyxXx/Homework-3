def main():
    shopping_list = list()

    while True:
        purchase = input("Add purchase: ")
        if not purchase:
            break

        if purchase in shopping_list:
            shopping_list.remove(purchase)
        else:
            shopping_list.append(purchase)

    print('----------------------------------------')
    for purchase in shopping_list:
        print(purchase)
    print('----------------------------------------')


if __name__ == '__main__':
    main()