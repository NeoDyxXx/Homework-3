def print_cat(message: str):
    margin = 15
    print("\n{0}{1}".format(" " * margin, "_" * message.__len__()))
    print("{0}< {1} >".format(" " * (margin - 2), message))
    print("{0}{1}".format(" " * margin, "-" * message.__len__()))
    print("{0}/".format(" " * (margin - 3)))
    print("  /\_/\ {0}/".format(" " * (margin - 12)))
    print(" ( \u00b0.\u00b0 )")
    print("  > ^ <")


def main():
    text = input("Print text: ")
    print_cat(text)


if __name__ == '__main__':
    main()