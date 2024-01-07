def inventory(player: object, enemy=None):
    while True:
        print("Things you can see in inventory:")
        for item in player.show_items_in_inventory():
            print(f"- {item}")
        print("What do you want to do?")
        print(" - Check item"
              "\n - Close inventory")
        action = str(input())
        if action.lower() == "check item":
            print("What item do you want to check?")
            item = input()
            if player.get_item_from_inventory(item):
                print(f"You check the {player.get_item_from_inventory(item)['item'].name} \n"
                      f"and you know this things about {player.get_item_from_inventory(item)['item'].name}: {player.get_item_from_inventory(item)['item'].description} \n"
                      f" and you have {player.get_item_from_inventory(item)['amount']} of them")
                print("You want to use it?")
                print(" - Yes"
                      "\n - No")
                action = str(input())
                if action.lower() == "yes":
                    print(f"You used the {player.get_item_from_inventory(item)['item'].name}")
                    if player.get_item_from_inventory(item)['item'].type == "Healing":
                        player.hp += player.get_item_from_inventory(item)['item'].use_value
                        print(f"You healed {player.get_item_from_inventory(item)['item'].use_value} hp")
                        player.remove_from_inventory(player.get_item_from_inventory(item)['item'])
                    elif player.get_item_from_inventory(item)['item'].type == "Damage":
                        if enemy:
                            enemy.hp -= player.get_item_from_inventory(item)['item'].use_value
                            print(
                                f"You did {player.get_item_from_inventory(item)['item'].use_value} damage to {enemy.name}")
                            player.remove_from_inventory(player.get_item_from_inventory(item)['item'])
                        else:
                            print("You don't have a target")
                    else:
                        print("That item can't be used")
                    if enemy: return True
                elif action.lower() == "no":
                    print(f"You didn't use the {player.get_item_from_inventory(item)['item'].name}")
            else:
                print("You don't have that item")
        elif action.lower() == "close inventory":
            print("You close your inventory")
            return True
        else:
            print("That is not a valid action")
