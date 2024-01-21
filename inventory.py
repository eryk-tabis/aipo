def inventory(player: object, enemy=None):
    while True:
        print("Rzeczy w Twoim plecaku:")
        for item in player.show_items_in_inventory():
            print(f"- {item}")
        print("Co chcesz zrobić?")
        print(" - Sprawdź rzecz (check)"
              "\n - Zamknij ekwipunek (close)")
        action = str(input()).lower()
        if action == "sprawdź rzecz" or action == "check":
            print("Którą rzecz chcesz sprawdzić?")
            item = input()
            if player.get_item_from_inventory(item):
                print(f"Sprawdzasz {player.get_item_from_inventory(item)['item'].name} \n"
                      f"Opis {player.get_item_from_inventory(item)['item'].name}: {player.get_item_from_inventory(item)['item'].description} \n"
                      f" i masz {player.get_item_from_inventory(item)['amount']} szt.")
                print("Chcesz to użyć")
                print(" - Tak"
                      "\n - Nie")
                action = str(input()).lower()
                if action == "tak":
                    print(f"Wykorzystałeś {player.get_item_from_inventory(item)['item'].name}")
                    if player.get_item_from_inventory(item)['item'].type == "Healing":
                        player.hp += player.get_item_from_inventory(item)['item'].use_value
                        print(f"Zostałeś uleczony o {player.get_item_from_inventory(item)['item'].use_value} hp")
                        player.remove_from_inventory(player.get_item_from_inventory(item)['item'])
                    elif player.get_item_from_inventory(item)['item'].type == "Damage":
                        player.equipped.damage += player.get_item_from_inventory(item)['item'].use_value
                        print(
                                f"Twój atak został zwiększony o {player.get_item_from_inventory(item)['item'].use_value} pkt.")
                    else:
                        print("Nie możesz użyć tego przedmiotu")
                    if enemy: return True
                elif action.lower() == "no":
                    print(f"Nie użyłeś {player.get_item_from_inventory(item)['item'].name}")
            else:
                print("Nie masz tego przedmiotu")
        elif action.lower() == "zamknij ekwipunek" or action == "close":
            print("Zamknąłeś ekwipunek")
            return True
        else:
            print("To nie jest prawidłowa akcja")
