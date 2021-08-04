"""
Classes for player, player gear, player inventory,
enemies, NPCs, weapons, armor, potions, and misc items.
"""

import os
import textwrap
from time import sleep
from random import randint, uniform

from engine.typewriter import *

class Player:
    """Manages player's general stats and options in combat."""

    def __init__(self, name: str, max_hp: float, hp: float, dmg: list, lvl: int,
                 xp: int, next_lvl: int, crit_chance: int, crit_dmg: float, start_room: str, has_dlc):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.dmg = dmg
        self.lvl = lvl
        self.xp = xp
        self.next_lvl = next_lvl
        self.crit_chance = crit_chance
        self.crit_dmg = crit_dmg
        self.start_room = start_room
        self.aurels = 1240
        self.hit_reduct = 0
        self.status_effects = False
        self.disease = None
        self.has_dlc = has_dlc

    def attack(self, target: object):
        """
        Picks dmg from lower/upper bound, checks for crit parameters, checks
        if player misses, then hits if not missed.
        """

        print("\nYou strike at the enemy!")
        damage = round(uniform(self.dmg[0], self.dmg[1]), 2)
        crit_check = randint(self.crit_chance, 100)
        miss_check = randint(1, 20)  # 20% chance to miss attack.
        if miss_check == 10:  # End turn if player misses.
            print("MISS!")
            return
        if crit_check <= self.crit_chance:  # Add crit dmg to dmg if crit.
            print("CRITICAL!")
            add_crit = round(damage * self.crit_dmg, 2)
            damage = round(damage + add_crit, 2)

        # Subtract total damage from target's hp.
        target.hp = round(target.hp - damage, 2)
        print(f"Damage given: {damage}")
        if target.hp <= 0:
            target.hp = 0
        print(f"Enemy HP: {target.hp}")

        return

    def flee(self, enemy: object) -> bool:
        """Returns True if successfully flees, False if not"""

        type("\nYou attempt to flee...\n")
        sleep(0.5)
        check_roll = randint(1, 2)  # 50% chance to flee.
        if check_roll == 1:
            return True
        else:
            return False

    def check_levelup(self) -> bool:
        """ Returns True if player leveled. Returns False if stayed the same.
        Checks to see if player has enough experience points to level up
        """

        has_leveled = False  # Flag to determine return output.
        while self.xp >= self.next_lvl:  # Loop until xp is less than xp to next level.
            os.system("cls")
            has_leveled = True
            self.lvl += 1
            self.xp = self.xp - self.next_lvl
            self.next_lvl = round(self.next_lvl * 1.5)

            # Display available stats to increase per level up.
            type(f"\nLevel up!\n")
            print(f"\nNew level: {self.lvl}\nXP to next level: {self.next_lvl}\n")
            print(f"1) +5.0 to max HP (current: {self.max_hp})")
            print(f"2) +0.2 to base damage (current: {self.dmg[0]}-{self.dmg[1]})")
            print(f"3) +2% chance to crit (current: {self.crit_chance}%)")
            print(f"4) +0.02 to crit damage (current: +{self.crit_dmg}% dmg if crit)")

            print("Choose one stat to increase (enter number):")
            while True:  # Loop for user choice.
                try:
                    chosen_stat = int(input("> ").strip())

                    if chosen_stat not in [1, 2, 3, 4]:
                        print("\nNot in list!")
                    else:
                        if chosen_stat == 1:
                            type(f"\nYour HP: {self.hp} -> {self.hp + 5.0}", 0.04, 0.04)
                            self.hp += 5
                        elif chosen_stat == 2:
                            type(f"\nYour damage: {self.dmg[0]}-{self.dmg[1]} -> {self.dmg[0] + 0.2}-{self.dmg[1] + 0.2 }", 0.04, 0.04)
                            self.dmg[0] = round(self.dmg[0] + 0.20, 2)
                            self.dmg[1] = round(self.dmg[1] + 0.20, 2)
                        elif chosen_stat == 3:
                            type(f"\nYour crit chance: {self.crit_chance}% -> {self.crit_chance + 2}%", 0.04, 0.04)
                            self.crit_chance += 2
                        elif chosen_stat == 4:
                            type(f"\nYour crit damange: +{self.crit_dmg}% -> +{self.crit_dmg + 0.02}%", 0.04, 0.04)
                            self.crit_dmg += 0.02
                        input("\n\nPress 'enter' to continue...")
                        break
                except ValueError:  # Only int values are allowed.
                    print("\nEnter only numbers!")

        if has_leveled:
            return True
        else:
            return False
            

    def check_stats(self) -> None:
        """Display health and stats"""

        os.system("cls")
        health = self.hp
        health_checks = {
            "check1": "You feel at your very best.",  # At least 95% of max health.
            "check2": "You feel good all around.",  # At least 75% of max health.
            "check3": "Could use a little potion, but you might get by.", # At least 50% of max health.
            "check4": "You're pretty hurt, got any potions laying around?",  # At least 25% of max health.
            "check5": "You're on the brink of death, try not to die!",  # Below 25% of max health.
            "checkx": f"You have an ongoing disease, {self.disease}. I suggest not moving too much.",  # Contracted disease.
            }

        # Display unique health description depending on hp amount in relation to max hp.
        if (not self.status_effects) and (self.hp >= round(self.max_hp * 0.95, 2)):
            print(f"\nYour health: {self.hp}. {health_checks['check1']}")
        elif (not self.status_effects) and (self.hp >= round(self.max_hp * 0.75, 2)):
            print(f"\nYour health: {self.hp}. {health_checks['check2']}")
        elif (not self.status_effects) and (self.hp >= round(self.max_hp * 0.50, 2)):
            print(f"\nYour health: {self.hp}. {health_checks['check4']}")
        elif (not self.status_effects) and (self.hp >= round(self.max_hp * 0.25, 2)):
            print(f"\nYour health: {self.hp}. {health_checks['check5']}")
        elif (not self.status_effects) and (self.hp < round(self.max_hp * 0.25, 2)):
            print(f"\nYour health: {self.hp}. {health_checks['checkx']}")
        elif self.status_effects:
            print(f"\nYour health: {self.hp}. {health_checks['checkx']}")
        else:
            print(f"\nYour health: {self.hp}.")

        # Display stats.
        print(f"\nName: {self.name}")
        print(f"Level: {self.lvl}")
        print(f"XP: {self.xp}")
        print(f"XP to level up: {self.next_lvl}")
        print(f"Damage: {self.dmg[0]}-{self.dmg[1]}")
        print(f"Critical chance: {round(self.crit_chance, 2)}% to crit")
        print(f"Critical damage: +{round(self.crit_dmg*100, 2)}% damage if crit")
        print(f"Damage reduction: -{round(self.hit_reduct*100, 2)}% damage from enemies")
        print(f"Disease: {self.disease}")

        input("\nPress enter to continue...")
        os.system("cls")

    def pick_up(self, item: object, player_inv: object, player_gear: object, initializing=False) -> None:
        """Sends item to inventory or gear to gear inventory"""

        try:  # Gear inventory.
            item.gear_type
            player_gear.gear_dict[item] = False
            if initializing is False:
                type(f"\n{item.name.title()} has been added to your gear.\n", 0.03)
                sleep(0.5)
        except AttributeError:  # Inventory.
            player_inv.items.append(item)
            if initializing is False:
                type(f"\n{item.name.title()} has been added to your inventory.\n", 0.03)
                sleep(0.5)
        return

class PlayerGear:
    def __init__(self):
        self.capacity = 15
        self.weapon = None
        self.head = None
        self.body = None
        self.feet = None
        self.hands = None

        # Keeps track of gear and gear info.
        # Key: gear name.
        # Value: True = equipped, False = not equipped.
        self.gear_dict = {}

    def view_gear(self, my_player: object) -> None:
        """Displays player gear, player choices, and gear stats."""

        os.system("cls")

        if not self.weapon and not self.head and not self.body and not self.feet and not self.hands:
            type("\nYour have nothing equipped.\n")

        # Gear slots and attached gear if any.
        name = "None" if not self.weapon else self.weapon.name
        print(f"\n    Weapon: {name.title()}")
        name = "none" if not self.head else self.head.name
        print(f"Head armor: {name.title()}")
        name = "None" if not self.body else self.body.name
        print(f"Body armor: {name.title()}")
        name = "None" if not self.hands else self.hands.name
        print(f"    Gloves: {name.title()}")
        name = "None" if not self.feet else self.feet.name
        print(f"  Footwear: {name.title()}")

        # Display gear (equipped or not).
        counter = 1
        gear_list = []
        gear_list_equipped = []
        print("\nGear list:")
        for gear, value in self.gear_dict.items():
            if value is True:
                print(f"{counter}] {gear.name.title()} - equipped")
            else:
                print(f"{counter}] {gear.name.title()}")
            gear_list.append(gear)
            gear_list_equipped.append(value)
            counter += 1
        print(f"{len(self.gear_dict)+1}] GO BACK")

        while True:  # Loop for player responses.
            try:
                print("\nEnter number on item list to view/perform action")
                user_num = int(input("> ").lower().strip())

                if user_num == len(self.gear_dict)+1:
                    print("Closing gear view...")
                    os.system("cls")
                    return
                elif user_num not in range(1, len(self.gear_dict)+1):
                    print("Not in list!")
                else:
                    os.system("cls")
                    break
            except ValueError:  # Only int values are allowed.
                print("Enter only numbers!")

        # Display gear stats and choices for player.
        gear = gear_list[user_num-1]  # Gear object.
        gear_equipped = gear_list_equipped[user_num-1]  # Gear True/False (equipped or not).
        gear_list_tuple = [("HE", "Head Armor"), ("B", "Body armor"), ("F", "Footwear"), ("HA", "Gloves")]
        print(gear.name.title())
        print("---------------")
        print(textwrap.fill(f"\n*{gear.desc}", 80))

        if gear.gear_type == "W":  # Unique display for weapons.
            print(f"- +{gear.dmg[0]}-{gear.dmg[1]} damage to base damage")
            print(f"- +{gear.plus_crit_chance}% chance to crit to base crit chance")
            print(f"- +{gear.plus_crit_dmg*100}% crit damage to base crit damage")
            print(f"- Value: {gear.worth} aurels\n")
        else:  # Unique display for body armor.
            section = None
            for part in gear_list_tuple:
                if gear.gear_type == part[0]:
                    section = part[1]
            print(f"- {section}")
            print(f"- +{gear.hit_reduct*100}% hit reduction to base")
            print(f"- Value: {gear.worth} aurels\n")

        if gear_equipped is False:  # Ask for choice depending on gear is equipped or not.
            print("Equip, drop, or go back?")
        else:
            print("Unequip, drop, or go back?")

        while True:  # Loop for player response.
            user_input = input("> ").lower().strip()
            if user_input == "go back":
                os.system("cls")
                self.view_gear(my_player)
                break

            elif user_input == "drop":
                self.drop(my_player, gear, gear_equipped)
                self.view_gear(my_player)
                break

            elif user_input == "equip":
                # Check if player is trying to wear DLC armor.
                if gear.name == "soulforged breastplate of the damned" and not my_player.has_dlc:
                    print("\nYou must purchase DLC in order to wear this!")
                    continue
                elif gear.name == "soulforged breastplate of the damned" and my_player.lvl != 50:
                    print("\nYou must be level 50 to equip!")
                    continue
                elif gear_equipped is True:
                    print("You cannot equip what's already equipped.")
                    continue
                else:  # Player equips gear.
                    os.system("cls")
                    sum_dict = {
                        "W": self.weapon,
                        "HE": self.head,
                        "B": self.body,
                        "F": self.feet,
                        "HA": self.hands,
                        }
                    for section, part in sum_dict.items():
                        if gear.gear_type == section and part is not None:
                            self.unequip(my_player, part)
                            self.equip(my_player, gear)
                            break
                    self.equip(my_player, gear)
                    self.view_gear(my_player)
                    break

            elif user_input == "unequip":
                if gear_equipped is False:
                    print("You cannot unequip what's not currently equipped.")
                else:
                    self.unequip(my_player, gear)
                    self.view_gear(my_player)
                    break
            else:
                print("\nInvalid or unknown input.")
                continue

    def equip(self, player: object, gear: object, initializing=False) -> None:
        """
        Assigns gear to correct place if player equips. Simulates 'wearing' it.
        Adds gear stats to player stats.
        """

        if gear.gear_type == "W":  # Weapon.
            if self.weapon is None:
                self.weapon = gear
                self.gear_dict[gear] = True
                player.dmg[0] += gear.dmg[0]
                player.dmg[1] += gear.dmg[1]
                player.crit_chance += gear.plus_crit_chance
                player.crit_dmg += gear.plus_crit_dmg
                print(f"\n{gear.name.title()} is now equipped.")
        elif gear.gear_type == "HE":  # Head.
            if self.head is None:
                self.gear_dict[gear] = True
                self.head = gear
                player.hit_reduct += gear.hit_reduct
                print(f"\n{gear.name.title()} is now equipped.")
        elif gear.gear_type == "B":  # Body.
            if self.body is None:
                self.gear_dict[gear] = True
                self.body = gear
                player.hit_reduct += gear.hit_reduct
                print(f"\n{gear.name.title()} is now equipped.")
        elif gear.gear_type == "HA":  # Hands.
            if self.hands is None:
                self.gear_dict[gear] = True
                self.hands = gear
                player.hit_reduct += gear.hit_reduct
                print(f"\n{gear.name.title()} is now equipped.")
        elif gear.gear_type == "F":  # Feet.
            if self.feet is None:
                self.gear_dict[gear] = True
                self.feet = gear
                player.hit_reduct += gear.hit_reduct
                print(f"\n{gear.name.title()} is now equipped.")

        if initializing:  # To not add delay effect if starting game.
            return
        else:
            sleep(1)

    def unequip(self, player: object, gear: object, initializing=False) -> None:
        """Negates everything equip() method does"""

        # Determine gear type, then unequip.
        if gear.gear_type == "W":
            if self.weapon is not None:
                self.weapon = None
                self.gear_dict[gear] = False
                player.dmg[0] -= gear.dmg[0]
                player.dmg[1] -= gear.dmg[1]
                player.crit_chance -= gear.plus_crit_chance
                player.crit_dmg -= gear.plus_crit_dmg
                print(f"\nYou take off {gear.name.title()}.")
        elif gear.gear_type == "HE":
            if self.head is not None:
                self.gear_dict[gear] = False
                self.head = None
                player.hit_reduct -= gear.hit_reduct
                print(f"\nYou take off {gear.name.title()}.")
        elif gear.gear_type == "B":
            if self.body is not None:
                self.gear_dict[gear] = False
                self.body = None
                player.hit_reduct -= gear.hit_reduct
                print(f"\nYou take off {gear.name.title()}.")
        elif gear.gear_type == "HA":
            if self.hands is not None:
                self.gear_dict[gear] = False
                self.hands = None
                player.hit_reduct -= gear.hit_reduct
                print(f"\nYou take off {gear.name.title()}.")
        elif gear.gear_type == "F":
            if self.feet is not None:
                self.gear_dict[gear] = False
                self.feet = None
                player.hit_reduct -= gear.hit_reduct
            print(f"\nYou take off {gear.name.title()}.")

        if initializing:  # To not add delay effect if starting game.
            return
        else:
            sleep(1)

    def drop(self, my_player: object, gear: object, gear_equipped: bool) -> None:
        """Takes out object from gearventory and deletes it"""

        print("\nWarning: Dropped gear and items cannot be retrieved back. Proceed? (Y/N)")
        while True:  # Loop for player response.
            user_input = input("> ").lower().strip()
            if user_input == "y":
                if gear_equipped is True:
                    self.unequip(my_player, gear)
                del self.gear_dict[gear]
                sleep(1)
            elif user_input == "n":
                return
            else:
                print("\nInvalid input.")
                continue
            return


class PlayerInventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []

    def view_inventory(self, my_player: object) -> bool:
        """ Returns True if player uses item. Returns False if not.
        Enumerates inventory items in a list with which player can interact
        """

        os.system("cls")
        performed = None
        if not self.items:  # Nothing in inventory.
            print(f"\nAurels: {my_player.aurels}")
            type("Your inventory is empty.\n")
            sleep(0.5)
        else:  # If stuff in inventory.
            os.system("cls")
            counter = 1
            print(f"\nAurels: {my_player.aurels}\n")
            for item in self.items:
                print(f"{counter}] {item.name.title()}")
                counter += 1
            print(f"{len(self.items)+1}] GO BACK")

            while True:  # Loop for player response.
                try:
                    print("\nEnter number on item list to do an action")
                    user_num = int(input("> ").lower().strip())

                    if user_num == len(self.items)+1:
                        print("\nClosing inventory...")
                        sleep(1)
                        os.system("cls")
                        return False
                    elif user_num not in range(1, len(self.items)+1):
                        print("Not in list!")
                    else:
                        os.system("cls")
                        break
                except ValueError:  # Only int values are allowed.
                    print("Enter only numbers!")

            # Player has selected an item.
            item = self.items[user_num-1]
            print(item.name.title())
            print("---------------")
            print(textwrap.fill(f"\n*{item.desc}", 80))
            while True:  # Loop for player response.
                print("\nUse, drop, or go back?")
                user_input = input("> ").lower().strip()

                if user_input == "go back":
                    os.system("cls")
                    self.view_inventory(my_player)
                    break
                elif user_input == "use":
                    performed = item.use(item, my_player)
                    if performed is False:
                        continue

                    self.drop(item, user_num, True)  # Player consumes.
                    break
                elif user_input == "drop":
                    if item.quest_item is True:
                        print("\nYou may not drop quest items")
                        continue
                    self.drop(item, user_num, False)
                    self.view_inventory(my_player)
                    break
                else:
                    print("\nInvalid input")

        return performed

    def drop(self, item: object, user_num: int, consumed: bool) -> None:
        """Takes out item from inventory and deletes it."""

        if not consumed:  # Loop for player validation.
            print("\nWarning: Dropped gear and items cannot be retrieved back. Proceed? (Y/N)")
            user_confirm = input("> ").lower().strip()

            if user_confirm == "y":
                popped_item = self.items.pop(user_num-1)
                del popped_item
            elif user_confirm == "n":
                return
            else:
                print("\nInvalid input")
        else:
            popped_item = self.items.pop(user_num-1)
            del popped_item



class Enemy:
    def __init__(self, name: str, hp: int, dmg: list, crit_chance: int,
                 crit_dmg: float, intro_desc: str, death_desc: str, aurels: int,
                 xp_drop: int, npc=None, player_can_flee=True):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.crit_chance = crit_chance
        self.crit_dmg = crit_dmg
        self.intro_desc = intro_desc
        self.death_desc = death_desc
        self.aurels = aurels
        self.xp_drop = xp_drop
        self.npc = npc
        self.player_can_flee = player_can_flee

    def attack(self, target: object) -> None:
        """
        Picks dmg from lower/upper bound, checks for critical, checks
        if misses, then hits if not missed.
        """

        print("\nThe enemy strikes you!")
        base_damage = randint(self.dmg[0], self.dmg[1])
        crit_check = randint(self.crit_chance, 100)
        miss_check = randint(1, 20)  # 20% chance to miss attack.
        if miss_check == 10:  # End turn if enemy misses.
            print("MISS!")
            return
        if crit_check <= self.crit_chance:  # Add crit dmg to dmg if crit.
            print("CRITICAL!")
            add_crit = base_damage * self.crit_dmg
            base_damage += round(add_crit, 2)

        # Subtracts total damage from target's hp.
        actual_damage = round((base_damage-(base_damage*target.hit_reduct)), 2)
        target.hp -= actual_damage
        target.hp = round(target.hp, 2)
        print(f"Damage received: {actual_damage}")
        if target.hp <= 0:
            target.hp = 0
        print(f"Your HP: {target.hp}")

        return


class NPC:
    def __init__(self, name: str):
        self.name = name

    def get_response(self, options: list) -> int:
        """ Returns player response int.
        Player has response choices after NPC talks.
        """

        valid_inputs = []
        print()
        # Display optional responses.
        for index, option in enumerate(options):
            print(f"{str(index+1)}] {option[0]}")
            valid_inputs.append(index+1)

        print("\nYou:")
        while True:  # Loop for valid response choice.
            try:
                user_input = int(input("> "))
            except ValueError:
                print("\nNot an option!")
            else:
                if user_input not in valid_inputs:
                    print("\nNot an option!")
                else:
                    return options[user_input-1][1]

    def dialogue_flow(self, convo: dict) -> int:
        """ Returns outcome int.
        Main function to operate convo with NPC.
        """

        current_page = 1
        while current_page != None:  # Loop through all NPC text.
            page = convo.get(current_page)

            if page == None:  # Flag to determine if convo is done.
                current_page = None
                break

            # Display dialogue.
            os.system("cls")
            print(f"\n{self.name.title()}:")
            type(f"{page['text']}\n")
            sleep(1)

            # Default is 0 for True and 1 for False.
            if page['options'] == 0:
                current_page = None
                return 0  # Conversation ends normally.
            elif page['options'] == 1:
                current_page = None
                return 1  # Initiate battle.
            elif page['options'] == 2:
                current_page = None
                return 2  # Special for ending.

            # Calls player response function.
            current_page = self.get_response(page['options'])


class Weapon:
    def __init__(self, name: str, desc: str, gear_type: str, dmg: list,
                 plus_crit_chance: int, plus_crit_dmg: float, worth: int):
        self.name = name
        self.desc = desc
        self.gear_type = gear_type
        self.dmg = dmg
        self.plus_crit_chance = plus_crit_chance
        self.plus_crit_dmg = plus_crit_dmg
        self.worth = worth


class Armor:
    def __init__(self, name: str, desc: str, gear_type: str,
                 hit_reduct: float, worth: int):
        self.name = name
        self.desc = desc
        self.gear_type = gear_type
        self.hit_reduct = hit_reduct
        self.worth = worth


class Potion:
    def __init__(self, name: str, desc: str,
                 worth: int, hp_add=0, quest_item=False, effect=None):
        self.name = name
        self.desc = desc
        self.worth = worth
        self.hp_add = hp_add
        self.quest_item = quest_item
        self.effect = effect

    def use(self, item: object, my_player: object) -> bool:
        """ Returns True if drank potion, False if not.
        Check which kind of potion is being drunk and add effects.
        """

        os.system("cls")

        print()
        if self.name == "cure disease potion":
            type(textwrap.fill("\nYou drink up the potion, heaving at its repulsive taste. You start to feel your disease slip away by the second.\n", 80))
            type(f"\n\n{my_player.disease.title()} removed.", 0.04, 0.75)
            my_player.disease = None
            my_player.status_effects = False

        if my_player.hp >= my_player.max_hp:
            type("Your health is already full!\n")
            return False  # Player doesn't drink potion.

        elif self.name == "small health potion":
            prev_hp = my_player.hp
            my_player.hp += self.hp_add
            if my_player.hp > my_player.max_hp:
                my_player.hp = my_player.max_hp
            print(f"Your HP: {prev_hp} -> {my_player.hp}\n")
            type(textwrap.fill("\nYou slurp up the vial and feel a noticeable but pleasant jolt.\n", 80))

        elif self.name == "medium health potion":
            prev_hp = my_player.hp
            my_player.hp += self.hp_add
            if my_player.hp > my_player.max_hp:
                my_player.hp = my_player.max_hp
            print(f"Your HP: {prev_hp} -> {my_player.hp}\n")
            type(textwrap.fill("\nYou pour the contents down your throat and feel a slight surge of energy.\n", 80))

        elif self.name == "large health potion":
            prev_hp = my_player.hp
            my_player.hp += self.hp_add
            if my_player.hp > my_player.max_hp:
                my_player.hp = my_player.max_hp
            print(f"Your HP: {prev_hp} -> {my_player.hp}\n")
            type(textwrap.fill("\nYou chug the potion all the way down and feel a burst of refreshing life.\n", 80))

        input("\n\nPress 'enter' to continue...")
        os.system("cls")

        return True  # Let game know that player drank potion, for combat purposes.


class MiscItem:
    def __init__(self, name: str, desc: str, worth: int, quest_item: bool):
        self.name = name
        self.desc = desc
        self.worth = worth
        self.quest_item = quest_item

    def use(self, item: object, my_player:object) -> bool:
        """ Returns False.
        More like to show usage.
        """
        if item.name == "large key" or item.name == "small key":
            print("\nTo use, go towards the locked door you wish to open.")
        return False
