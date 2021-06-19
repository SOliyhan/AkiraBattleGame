# Simple Battle Game of points over selection of types of attack(from a list) in a fight.

import random
import time

def space():
    print(" ")

def sleep():
    time.sleep(1.3)

def result(name,player, monster):
    if player < 1:
        sleep()
        print(f"{name} lose...")
    elif monster < 1:
        sleep()
        print(f"{name} wins!!")
        #return player, monster


def monsterAttack(name,player,monster_choosen):
    print("=======================")
    space()
    print(f"{monster_choosen} time!")
    sleep()
    space()

    attack_choice = random.randint(1,3)
    if attack_choice == 1:
        print(f"{monster_choosen} dealt 10 damage!")
        player1 = player - 10
        sleep()
        print(f"{name} have {player1} life now!")
        space()
    elif attack_choice == 2:
        print(f"{monster_choosen} dealt 15 damage!")
        player1 = player - 15
        sleep()
        print(f"{name} have {player1} life now!")
        space()
    elif attack_choice == 3:
        print(f"{monster_choosen} dealt 20 damage!")
        player1 = player - 20
        sleep()
        print(f"{name} have {player1} life now!")
        space()
    return player1


# player attack
def playerAttack(name,player,monster_choosen,monster):
    while player > 1:
        time.sleep(1)
        print("=======================")
        space()
        print(f"{name}'s life: {player}\n{monster_choosen}'s life: {monster}")
        space()
        sleep()
        print(f"What will {name} do?")
        attack = int(input("[1] Normal Attack\n[2] Special Attack\n[3] Recover life\n>>> "))
        space()
        if attack == 1:
            sleep()
            print(f"{name} dealt 15 damage!")
            monster = monster - 15
            sleep()
            print(f"{monster_choosen} have {monster} life now!")
            space()

        elif attack == 2:
            sleep()
            chance = random.randint(1,2)
            if chance == 1:
                print(f"{name} dealt 35 damage!")
                monster= monster - 35
                sleep()
                print(f"{monster_choosen} have {monster} life now!")
                space()
            else:
                print(f"{name} failed!")

        elif attack == 3:
            sleep()
            print(f"{name} recovered 30 life!")
            sleep()
            player = player + 30
            print(f"{name} have {player} life now!")

        # monster attack
        if monster>1:
            player = monsterAttack(name, player, monster_choosen)
        elif player<1 or monster<1:
            break

    result(name, player, monster)


print("--------Simple Battle Game-----------")
name = input("What is your name\n>>> ")
monster_list = ["spider", "mad eye", "zombie", "skeleton", "Swordfish"]
monster_choosen = random.choice(monster_list)
print(f"a '{monster_choosen}' appeared for battle!")
player = 100
monster = 100

playerAttack(name, player, monster_choosen, monster)