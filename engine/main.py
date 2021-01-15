# -*- coding: utf-8 -*-
"""
Main engine module, brings everything together.
"""

import os
import sys
import time
import random
import textwrap

import engine.map_layout as ml
import engine.npc_dialogue as nd
from engine.initiate import *
from engine.instances import *
from engine.typewriter import *
from engine.ending_sequence import *
from engine.classes import Player, PlayerInventory, PlayerGear, Weapon, Armor, Potion

### STATS ###


num_moves = 0
rooms_examined = 0
max_examine = 1  # Had to add this due to recursion.
score = (500 - my_player.hp) + num_moves


### INTERACTIVITY ###


def print_score():
    print(f"Score: {score} (lower is better)")
    print(f"Moves made: {num_moves}")
    print(f"Rooms examined: {rooms_examined}/12")


def death_sequence():
    type("\nY O U  A R E  D E A D\n", 0.05, 0)
    time.sleep(1)
    print_score()
    sys.exit()


def roll_dice(lower, upper):
    return random.randint(lower, upper)


def check_for_trap(my_player, current_room):
    trapped = ml.room_list[current_room][ml.b_trapped]
    if trapped:
        if current_room == "c4":
            print("\nYou've sprung a trap! A chained spiked ball is ejected at you and hits your head.")
            damage = roll_dice(5, 10)
            my_player.hp -= damage
            print(f"-{damage} to hp.")

        elif current_room == "b2":
            
            spider_drop = """You've sprung a trap! Darts fly out from every direction towards you, piercing
you through your armor and clothes. You stagger and curse at the initial pain
and quickly pluck out the darts. It didn't take you long to realize that from
one of your previous adventures you've felt this feeling before--you've
contracted scrittles.

Find something that can cure you."""
            
            print(spider_drop)
            print("Effect: -2 hp per movement.")
            my_player.status_effects = True
            my_player.disease = "scrittles"

        if my_player.hp <= 0:
            my_player.hp = 0
            print("\nAnd it was effective...")
            print(f"Your health: {my_player.hp}")
            death_sequence()
            
        ml.room_list[current_room][ml.b_trapped] = False
        ml.room_list[current_room][ml.hotspot] = False
        input("\nPress 'enter' to continue...")
        os.system("cls")
        return
    else:
        return


def necromancer_meeting(current_room, npc, boss):
    """Ending stage of game
    Outcome 0) Player immediately fights necromancer at the start
    Outcome 1) Player fights necromancer even after hearing the truth.
    Outcome 2) Player joins necromancer after hearing the truth.
    """

    os.system("cls")
    print()
    type(ml.room_list[current_room][ml.DESC])
    input("\n\nHit 'enter' to proceed...")
    os.system("cls")
    
    check_outcome = npc.dialogue_flow(nd.necromancer_dialogue)
    if check_outcome == 0:
        combat_sequence(boss, current_room)
        return 0  # Player kills necromancer, blissfully unaware of the truth.
    elif check_outcome == 1:
        combat_sequence(boss, current_room)
        return 1  # Player kills necromancer, but now aware of the truth.
    del npc
    del boss

    if check_outcome == 2:
        return 2  # Player joins necromancer after hearing the truth.


def chance_meeting(current_room):
    """A small chance that you'd encounter one of these NPCs"""
    global gay_rat_npc
    global gay_rat_enemy
    num = roll_dice(1, 50)

    if ml.room_list[current_room][ml.hotspot] is False:
        if num == 25:  # 1 in 50 chance of chance meeting per movement.
            try:
                if gay_rat_enemy.hp != 0:
                    print("\nSuddenly, a giant rat comes scurrying out of a hole in the wall and stops in\n\
front of you. Before you take out your sword, it speaks to you in a pipsqueak\n\
voice.")
                time.sleep(1)
                check_outcome = gay_rat_npc.dialogue_flow(nd.gay_rat_dialogue)
            except NameError:  # Intentionally raise this if player defeats gay rat.
                return
            else:
                # If not ran, means player has chosen to end convo peacefully.
                if check_outcome == 1:  # Player has chosen to initiate battle.
                    combat_sequence(gay_rat_enemy, current_room)
                del gay_rat_npc
                del gay_rat_enemy
                os.system("cls")
                return
        else:
            return
    else:
        return

def examine_room(my_player, current_room, player_inv, player_gear):
    """Takes boolean value and current room of player"""
    global rooms_examined
    global max_examine
    item_list = ml.room_list[current_room][ml.items]


    def view_items(my_player, current_room, item_list, player_inv, player_gear):
        counter = 1
        for item in item_list:
            print(f"{counter}] {item.name.title()}")
            counter += 1
        print(f"{counter}] GO BACK")

        print("\nSelect number of item list to perform action")
        while True:
            try:
                user_num = int(input("> ").lower().strip())
                if user_num == counter:
                    print("Closing items list...")
                    os.system("cls")
                    return
                elif user_num not in range(1, len(item_list)+1):
                    print("Not in list!")
                else:
                    os.system("cls")
                    break
            except:
                print("Enter only numbers!")

        item = item_list[user_num-1]
        print(item.name.title())
        print("---------------")
        print(textwrap.fill(f"\n*{item.desc}", 80))
        print("\nPick up or go back?")
        while True:
            user_input = input("> ")
            if user_input == "pick up":
                print("\n*Picks up*")
                my_player.pick_up(item, player_inv, player_gear)
                item_list.remove(item)
                examine_room(my_player, current_room, player_inv, player_gear)
                break
            elif user_input == "go back":
                os.system("cls")
                examine_room(my_player, current_room, player_inv, player_gear)
                break
            else:
                print("\nInvalid input.")
        return


    # If room has not yet been examined.
    if not ml.room_list[current_room][ml.examined]:
        os.system("cls")
        rooms_examined += max_examine
        max_examine = 0
        print("\nYou examine this room...")
        if item_list:
            print("\nand find the following item(s):")
            view_items(my_player, current_room, item_list, player_inv, player_gear)
        else:
            print("\nand there is nothing to pick up from this room.")

    # If room has already been examined.
    else:
        os.system("cls")
        if item_list:
            print("\nYou have already examined this room, but there are still items left to pick up:")
            view_items(my_player, current_room, item_list, player_inv, player_gear)
        else:
            print("\nYou have already examined this room.")

    ml.room_list[current_room][ml.examined] = True


def first_move(enemy):
    """Returns if player goes first; if enemy is first, does an attack then returns"""
    if roll_dice(1, 2) == 1:  # Player goes first.
        print("\nYou go first!")
        return
    else:  # Enemy goes first.
        print(f"\n{enemy.name.title()} goes first!")
        enemy.attack(my_player)
        return


def combat_sequence(enemy, current_room):
    """Returns True if enemy dies, calls death sequence if player dies, else returns if nothing happens"""
    os.system("cls")

    if enemy.name == "necromancer":  # Intro description of final boss before fight.
        type(textwrap.fill(f"\n{enemy.intro_desc}\n", 80))
    
    finished = False
    command_list = ("help", "attack", "flee", "gear", "inventory")

    def check_death(enemy, my_player):
        if enemy.hp <= 0:
            print()
            type(textwrap.fill(enemy.death_desc, 80))
            print()
            time.sleep(1)
            print(f"\nThe {enemy.name} has been slain!")
            print(f"Your remaining health: {my_player.hp}")
            return True
        elif my_player.hp <= 0:
            death_sequence()
        else:
            return

    first_move(enemy)
    print("Enter 'help' for options.")
    while not finished:
        check_death(enemy, my_player)
        print("\nWhat do you do?")
        user_input = input("> ").lower().strip()

        if user_input in command_list:
            if user_input == "attack":
                my_player.attack(enemy)
                # True = enemy slain.
                if check_death(enemy, my_player) == True:

                    # Give player dropped aurels if any.
                    aurels_dropped = enemy.aurels
                    if aurels_dropped > 0:
                        my_player.aurels += aurels_dropped
                        print(f"\nYou picked up {aurels_dropped} aurels.")
                        time.sleep(1)
                    # Give player xp after enemy defeat.
                    xp_dropped = enemy.xp_drop
                    if xp_dropped > 0:
                        my_player.xp += xp_dropped
                        print(f"\nYou absorbed {xp_dropped} xp from the battle.")
                        time.sleep(1)

                    input("\nPress 'enter' to continue...")
                    os.system("cls")

                    my_player.check_levelup()  # Checks to see if player leveled up.
                    os.system("cls")
                    return

                time.sleep(1.5)
                enemy.attack(my_player)

            elif user_input == "flee":
                flee = my_player.flee(enemy)  # Is returned True if player passes flee check.
                # If enemy attribute allows player to flee from battle and if also passes flee check.
                if flee is True and enemy.player_can_flee is True:
                    ml.room_list[current_room][ml.met_enemy] = True
                    print("\nFlee successful!")
                    time.sleep(1)
                    os.system("cls")
                    return False
                elif not enemy.player_can_flee:  # If enemy attribute doesn't allow fleeing (final boss).
                    print("\nYou may not flee from this enemy!")
                else:
                    print("\nFlee unsuccessful!")  # Flee check not passed.
                    time.sleep(1)
                    enemy.attack(my_player)

            elif user_input == "inventory":
                performed = player_inv.view_inventory(my_player)
                if performed is True:
                    time.sleep(1)
                    enemy.attack(my_player)

            elif user_input == "gear":
                player_gear.view_gear(my_player)

            elif user_input == "help":
                print(f"\nAvailable choices:\n{', '.join(command_list)}")
        else:
            print("\nUnknown or invalid command!")


def move_direction(current_room, DIRECTION):
    """
    Changes current room to next room and transfers the player there by returning next room.
    If player cannot go there, return same room.

    DIRECTION can be: NORTH, EAST, SOUTH, or WEST
    """
    global num_moves

    os.system("cls")
    
    next_room = DIRECTION
    if not next_room:  # There's no door that way.
        os.system("cls")
        print("\nYou cannot go that way.")

    elif ml.room_list[next_room][ml.locked]:  # If room is locked.
        # Key check to unlock storage room.
        if ml.room_list[next_room][ml.ROOM_NAME] == "storage room" and ml.storage_key not in player_inv.items:
            print("\nYou turn the knob and notice that it's locked. Maybe there's a key?")
            return current_room
        elif ml.room_list[next_room][ml.ROOM_NAME] == "storage room" and ml.storage_key in player_inv.items:
            num_moves += 1
            print("\nYou use the small key that you found to unlock the door.")

        # Key check to unlock laboratory room.
        if ml.room_list[next_room][ml.ROOM_NAME] == "spells and alchemy lab" and ml.storage_key in player_inv.items and ml.lab_key not in player_inv.items:
            print("\nYou try to use the small key but it doesn't fit the lock.")
            return current_room
        elif ml.room_list[next_room][ml.ROOM_NAME] == "spells and alchemy lab" and ml.lab_key not in player_inv.items:
            print("\nYou turn the knob and notice that it's locked. Maybe there's a key?")
            return current_room
        elif ml.room_list[next_room][ml.ROOM_NAME] == "spells and alchemy lab" and ml.lab_key in player_inv.items:
            num_moves += 1
            print("\nYou use the large key that you found to unlock the door.")

        ml.room_list[next_room][ml.locked] = False  # No longer need to unlock door key.
        current_room = next_room
        chance_meeting(current_room)  # Try a chance meeting for NPC.

    else:  # Player successfully moves to other, non-locked room.
        os.system("cls")
        num_moves += 1
        current_room = next_room
        chance_meeting(current_room)

    if my_player.disease == "scrittles":  # Checks if player has disease to subtract from hp.
        my_player.hp = round(my_player.hp - 2.00, 2)
        print("\nScrittles inflicts. You lost 2 hp.")
        if my_player.hp <= 0:
            print("\nYou have succumbed to Scrittles.")
            death_sequence()

    return current_room


### CORE GAME ###


def dungeon_loop():
    """
    Main engine loop where the player roams around the dungeon and interacts with environment. Interactions are
    modularized as functions (see above) that are called throughout gameplay.

    Game ends: 1) player dies or 2) player quits or 3) player defeats the necromancer.
    """
    global num_moves
    global rooms_examined
    global max_examine
    os.system("cls")
    command_list = ("help", "examine", "gear", "inventory", "stats", "go north", "go east", "go south", "go west")
    finished = False

    current_room = my_player.start_room
    prev_room = None
    while not finished:
        max_examine = 1

        # Checks to see if player leveled up.
        check_levelup = my_player.check_levelup()
        if check_levelup is True:
            os.system("cls")
            check_levelup = False

        check_for_trap(my_player, current_room)  # Checks for trap.

        if ml.room_list[current_room][ml.has_enemy]:
            room_enemy = ml.room_list[current_room][ml.enemy]  # Placeholder variable for enemy.

            if room_enemy.name == "necromancer":  # If player finally meets lair boss.
                ending = necromancer_meeting(current_room, necromancer_npc, necromancer)
                return ending

            if ml.room_list[current_room][ml.met_enemy] is False:  # If player has never met enemy.
                print()
                type(textwrap.fill(room_enemy.intro_desc, 80))
                print("\n\nYou unsheath your sword and prepare for combat")
            else:  # If player returns back to fighting enemy after fleeing.
                print(f"\n\nYou come back to face the {room_enemy.name}.")

            # Initiate combat with player.
            input("\nPress 'enter' to continue...")
            os.system("cls")
            combat_outcome = combat_sequence(room_enemy, current_room)  # combat_outcome - False: fleed battle (back to previous room), True: slain enemy.
            if combat_outcome is False:  # Fleed from enemy.
                num_moves += 1
                current_room = prev_room
                print(f"\nYou are back in the {ml.room_list[current_room][ml.ROOM_NAME]}")
            else:  # Slain enemy.
                ml.room_list[current_room][ml.has_enemy] = False
                ml.room_list[current_room][ml.hotspot] = False
                os.system("cls")

        # Outputs room description if player's first time there.
        if not ml.room_list[current_room][ml.passed] and check_levelup is False:
            print(f"\n{ml.room_list[current_room][ml.DESC]}")
            ml.room_list[current_room][ml.passed] = True
        else:
            print(f"\n{ml.room_list[current_room][ml.DESC]}")


        print("\nWhat do you do? (type 'help' for options)")
        user_input = input("> ").lower().strip()

        if user_input == "quit":  # Exits out of the game.
            print("\nAre you sure you want to quit the game? (Y/N)")
            print_score()
            while True:
                answer = input("> ").lower().strip()
                if answer == "y":
                    sys.exit()
                else:
                    os.system("cls")
                    break
        elif user_input in command_list or user_input == "monkey":

            if user_input == "help":
                os.system("cls")
                print(f"\nAvailable choices:\n{', '.join(command_list)}")

            elif user_input == "examine":
                examine_room(my_player, current_room, player_inv, player_gear)

            elif user_input == "stats":
                my_player.check_stats()

            elif user_input == "inventory":
                player_inv.view_inventory(my_player)

            elif user_input == "gear":
                player_gear.view_gear(my_player)

            elif user_input == "go north":
                prev_room = current_room
                current_room = move_direction(current_room, ml.room_list[current_room][ml.NORTH])

            elif user_input == "go east":
                prev_room = current_room
                current_room = move_direction(current_room, ml.room_list[current_room][ml.EAST])

            elif user_input == "go south":
                prev_room = current_room
                current_room = move_direction(current_room, ml.room_list[current_room][ml.SOUTH])

            elif user_input == "go west":
                prev_room = current_room
                current_room = move_direction(current_room, ml.room_list[current_room][ml.WEST])

            elif user_input == "monkey":
                os.system("cls")
                print("\nOOH OOOH AH AHH")

        else:
            os.system("cls")
            print("\nInvalid or unknown input.")


def main():
    # Equipping player items before entering lair.
    player_gear.equip(my_player, footman_sword, True)
    player_gear.equip(my_player, padded_armor, True)
    my_player.pick_up(small_health_potion, player_inv, player_gear)

    os.system("cls")

    intro_sequence()
    conclusion = dungeon_loop()
    if conclusion == 0:
        ending_sequence(0)
    elif conclusion == 1:
        ending_sequence(1)
    elif conclusion == 2:
        ending_sequence(2)
    
    os.system("cls")
    print("\nThanks for playing!")
    print_score()
    input()
    
    return
