def main():
    shopping_list = set()

    while True:
        purchase = input("Add purchase: ")
        if not purchase:
            break

        shopping_list.add(purchase)

    print('----------------------------------------')
    for purchase in shopping_list:
        print(purchase)
    print('----------------------------------------')


if __name__ == '__main__':
    main()