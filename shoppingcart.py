def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1]
    item = line[2:]

    return command, item


def process_order(order, cart):
    command, item = order

    if command == "a":
        print("Item added!")
        cart.add(item)
    elif command == "d" and item in cart:
        print("Item deleted")
        cart.remove(item)
    elif command == "q":
        return False

    return True    


def go_shopping():
    cart = set()

    while True:
        order = get_order()
        if not process_order(order, cart):
            break

    print(cart)
    print("finished")

go_shopping()
# print("Welcome to your shopping cart")


# def process():
#     print ("To add item to list write 'a', to delete item from cart write 'd', to quit press 'q'")
#     letter = input()
#     cart = []
#     shopping = True
#     while shopping:
#         if letter == "a":
#             print("Enter your cart item")
#             item = input()
#             if item == "q":
#                 return False
#             cart.append(item)
#             print("Your item " + item + " has been added. Things on your list:", "".join(cart))

#         elif letter == "d":
#             print("Which item do you want to delete? " + "".join(cart))
#             print (cart)
#             deleted_item = input()
#             cart.remove(deleted_item)
#             if deleted_item  == "q":
#                 return False

#         elif letter == "q":
#             return False



# process()
