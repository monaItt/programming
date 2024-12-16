def print_christmas_tree(height):
    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        print("*" * (2 * i - 1))

    for i in range(height - 1):
        print(" " * (height - 1) + "|")

tree_height = int(input("Gebe die Höhe des Baumes an: "))
print_christmas_tree(tree_height)