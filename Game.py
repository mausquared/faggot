import sys
import os
import random
import time

weapons = {"Rusty Sword": 0, "Great Sword": 40} # to add new things make new one, or add weapons onto dictionary than define in property and add to Player class

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 1
        self.weap = ["Rusty Sword"]
        self.curweap = self.weap[0]

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 6

        if self.curweap == "Great Sword":
            attack += 15

        return attack

class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 4                 # attack has to be whole number for it to / 2, only takes integers
        self.goldgain = 10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 8
        self.goldgain = 15
ZombieIG = Zombie("Zombie")

def main():
    print ("Welcome to my game")
    print ("1.) Start")
    print ("2.) Load")
    print ("3.) Exit")
    option = input("--> ")
    print('\n' * 80)
    if option == "1":
       start()
    elif option == "2":
       pass
    elif option == "3":
        sys.exit
    else:
        main()

def start():
    print ("Hello what is your name")
    option = input("--> ")
    print('\n' * 80)
    global PlayerIG
    PlayerIG = Player(option)
    start1()


def start1():
    print(f"Hello {PlayerIG.name} how are you?")
    print(f'Your gold is {PlayerIG.gold}')
    print(f'Your potions are {PlayerIG.pots}')
    print(f'Current weapons: {PlayerIG.curweap}')
    print(f"Health: {PlayerIG.health} / {PlayerIG.maxhealth}")
    print(f'Your attack stat is {PlayerIG.attack}')
    print("1.) Fight")
    print("2.) Store")
    print("3.) Inventory")
    print("4.) Save")
    print("5.) Exit")
    option = input("--> ")

    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        inventory()
    elif option == "4":
        sys.exit()
    else:
        start1()

def inventory():
    print("What do you want to do?")
    print("1.) Equip Weapon")
    print("2.) Back")
    option = input(">>> ")
    if option == '1':
        equip()
    elif option =='2':
        start1()

def equip():
    print('What do you want to equip?')
    for weapon in PlayerIG.weap:
        print(weapon)
    print("b to go back")
    option = input(">>> ")




def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if  enemynum == 1:
        enemy = GoblinIG
    else:
        enemy = ZombieIG
    fight()

def fight(empty=True):
    if empty:
        print("\n" * 80)
    print(f"\n{PlayerIG.name}              vs               {enemy.name}")
    print(f"{PlayerIG.name}'s {PlayerIG.health} / {PlayerIG.maxhealth}        {enemy.name}'s {enemy.health} / {enemy.maxhealth}")
    print(f"Potions {PlayerIG.pots}\n")
    print ("1.) Attack")
    print ("2.) Drink Potion")
    print ("3.) Run")
    option = input(">>> ")
    if option == "1":
        attack()
        print('\n')
        fight()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack) # Lowest attack divided by two, highest attack is default attack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print("You miss!")
    else:
        enemy.health -= PAttack
        print(f"You deals {PAttack} damage!")
    if enemy.health <= 0:
        win()

    if EAttack == enemy.attack/2:
        print("The enemy missed!")
    else:
        PlayerIG.health -= EAttack
        print(f"The Enemy {EAttack} deals damage")
    if PlayerIG.health <= 0:
        dead()
    else:
        time.sleep(1)
        fight()


def drinkpot():
    print('\n' * 80)
    if PlayerIG.pots == 0:
        print("You don't have any potions\n")
        fight(False)
    else:
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth

        print ("You drank a potion!\n")

        PlayerIG.pots -= 1
        fight(False)

def run():
    print('\n' * 80)
    runnum = random.randint(1, 3) # 1 in 3 change of getting away
    if runnum == 1:
        print('You have sucesfully ran away')
        option = input()
        start1()
    else:
        print('You have failed to get away')
        option = input()
        print('\n' * 80)
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack / 2:
            print("The enemy missed!")
        else:
            PlayerIG.health == EAttack
            print(f"The Enemy {EAttack} deals damage")
            option = input(' ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()


def win():
    print('\n' * 80)
    enemy.health = enemy.maxhealth
    print(f'You have defeated the {enemy.name}')
    print(f'You found gold {enemy.goldgain}')
    PlayerIG.gold += enemy.goldgain
    option = input('')
    start1()

def dead():
    print('\n' * 80)
    print("You have died")
    option = input('')

def store(clear=True):
    if clear:
        print('\n' * 80)
    print(f'Welcome to the shop, you have {PlayerIG.gold} to spend!')


    count = 1
    store_items = []
    for item in weapons:
        if item not in PlayerIG.weap:
            print(f"{count}.) {item} / {weapons[item]} gold")
            store_items.append(item)
            count += 1

    if len(store_items) == 0:
        print('There are no items left to buy, please go back.')
    else:
        print('What would you like to buy?')


    option = input()

    if option == 'back':
        start1()

    else:

        if int(option) < 1 or int(option) > len(store_items):
            print("Item does not exist, please select another.")
            option = input(" ")
            store()
            return

        option = store_items[int(option) - 1]
        if PlayerIG.gold >= weapons[option]:
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option) # adds weapon to inventory when said items is bought
            print(f"You have bought {option}")
            print('\n')
            store(False)

        else:
            print("You don't have enough gold")
            option = input(' ')
            store(False)




main()