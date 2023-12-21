def fight(player, enemy):
    """Fight the enemy"""
    print(f"You encounter an {enemy.name}")
    while enemy.hp > 0:
        print(f"It is your turn, you have {player.hp} hp and the enemy has {enemy.hp} hp, what do you want to do?")
        print(f"\n - Attack"
              f"\n - Open inventory")
        action = input()
        if action == "Attack":
            # enemy.hp -= player.attack
            print(f"You attack the {enemy.name} with {player.equipped.name} and it has {enemy.hp} hp left")
        elif action == "Open inventory":
            pass
       # player.set_hp(player.get_hp() - enemy.attack)
        print(f"Enemy attack you with {enemy.equipped.name} and you have {player.hp} hp left")