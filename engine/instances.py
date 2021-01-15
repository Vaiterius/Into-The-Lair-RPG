"""
Set descriptions for objects and create instances

Takes info from config file and applies to player's starting stats,
then initialize.
"""

import os
import sys
import textwrap
from configparser import ConfigParser

from engine.classes import *
from engine.typewriter import *

config = ConfigParser()
ini_file = "engine/data/config.ini"
config.read(ini_file)

### OBJECT DESCRIPTIONS ###
# Gear.
FOOTMAN_SWORD_DESC = "Standard issue infantry sword. Iron and very basic."
FINE_STEEL_SWORD_DESC = "Not your typical grunt sword. Tempered steel and comfortable grip."

PADDED_ARMOR_DESC = "Cheaply made woolen gambeson. Lightly padded. A bit worn out."
CHAINMAIL_ARMOR_DESC = "Protective steel-chained mesh matieral. Great against hand weapons, not so much against wyverns."
DLC_ARMOR_DESC = "Forged by lucifer himself from the depths of hell and infused with 10,000 souls of the damned, this chestpiece reigns above all in almost every aspect. Requires purchase of Demons & Gods DLC ($14.99) and must be level 100 to equip."
LEATHER_CAP_DESC = "Some leather over your head. What more do you expect?"
SCALE_MITTENS_DESC = "Faux wyvern scales. Forest colored and durable."
HUNTING_BOOTS_DESC = "Made for hunters, by hunters. Leather with some inside cushion."

# Items.
SMALL_HEALTH_POTION_DESC = "Small, red vial that restores hp when consumed. Heals 10 hp."
MEDIUM_HEALTH_POTION_DESC = "Medium, red vial that restores hp when consumed. Heals 25 hp."
LARGE_HEALTH_POTION_DESC = "Large, red vial that restores hp when consumed. Heals 50 hp."
CURE_DISEASE_POTION_DESC = "A white vial that cures most but not all diseases. May not taste good."

### ENEMY INTRO/DEATH DESCRIPTIONS ###
# wraith
WRAITH_INTRO_DESC = "As you step into the hallway, in front of you materializes a specter resembling a howling young woman in tattered clothes and wielding a rusty blade. She notices you and her expression quickly turns from mournful to enraged, and lunges."
WRAITH_DEATH_DESC = "You take the final jab at the wraith and an ear-piercing screech fills the hall as her whole form collapses to the ground, leaving only elemental dust and her tattered clothes. You know that wraiths haunt the places where they died and only still linger in the overworld for a reason. Perhaps the woman never got to tell her lover that she loved him before he perished in the area? Or perhaps her body and soul were being held against her will by some dark mage for their sick and twisted experiments?"

# giant rat
GIANT_RAT_INTRO_DESC = "You spot a large, black rodent in the corner of the hallway picking at scraps and grub from the floor before finally noticing you and stopping. It didn't care how much bigger you are than it and viciously starts scurrying at you, eyes blood red."
GIANT_RAT_DEATH_DESC = "A couple hits was all it took for the giant rat to fall under the hands of you and your mighty sword. That pest was no match for you!"
GAY_RAT_DEATH_DESC = "Well that didn't take long to finish. This was a 1 in 50 chance of meeting the NPC. Nice."

# ghoul
GHOUL_INTRO_DESC = "Immediately after opening the door you are taken aback by a putrid stentch of death before even noticing all the bones, body parts, and rotten corpses of humans and creatures that lay across the floor. Then, a humanoid figure of sunken flesh and barely intact eyeballs springs up from one of the piles, snatches a look at you, and pounces."
GHOUL_DEATH_DESC = 'It was a gruesome battle with the ghoul which left you wounded in all places it scratched and bit, but you managed to put it down once and for all. Out of breath and with gory scum and goop all over your attire, you stare at the macabre scene in the room and think, "What sick bastard lives in this hellhole?!"'

# necromancer
NECROMANCER_INTRO_DESC = "The necromancer lets out a menacing laugh and charges himself up with self-casted spells. You prepare yourself against whatever the necromancer conjures up for you."
NECROMANCER_DEATH_DESC = "At last, the necromancer falls to the ground defeated and lifeless. Your job here is done."

# skeleton
SKELETON_INTRO_DESC = "Upon entering the dungeon room, a wandering human skeleton stops in its tracks and turns around to you. Its eye sockets begin to glow bright red and the skeleton takes out its sword kept handily in its ribcage and marches towards you."
SKELETON_DEATH_DESC = "Bone is hard, but not hard enough. The skeleton disassembles to the ground and the faint glow of the eye sockets fades away."


### CREATE INSTANCES ###
player_name = ""  # Will be overidden by game intro.

# Set player stats.
max_hp = config.getfloat("Player stats", "max_hp")
hp = config.getfloat("Player stats", "hp")
lower_dmg = config.getfloat("Player stats", "lower_dmg")
upper_dmg = config.getfloat("Player stats", "upper_dmg")
lvl = config.getint("Player stats", "lvl")
xp = config.getint("Player stats", "xp")
next_lvl = config.getint("Player stats", "next_lvl")
crit_chance = config.getint("Player stats", "crit_chance")
crit_dmg = config.getfloat("Player stats", "crit_dmg")
start_room = config.get("Other", "start_room")
has_dlc = config.getboolean("Other", "has_dlc")

my_player = Player(player_name.title(), max_hp, hp, [lower_dmg, upper_dmg], lvl, xp, next_lvl, crit_chance, crit_dmg, start_room, has_dlc)
player_inv = PlayerInventory(15)
player_gear = PlayerGear()

# Gear.
footman_sword = Weapon("footman sword", FOOTMAN_SWORD_DESC, "W", [5.00, 6.00], 2, 0.05, 25)
fine_steel_sword = Weapon("fine steel sword", FINE_STEEL_SWORD_DESC, "W", [7.00, 9.00], 4, 0.10, 40)

padded_armor = Armor("padded armor", PADDED_ARMOR_DESC, "B", 0.10, 50)
chainmail_armor = Armor("chainmail body armor", CHAINMAIL_ARMOR_DESC, "B", 0.15, 80)
dlc_armor = Armor("soulforged breastplate of the damned", DLC_ARMOR_DESC, "B", 0.80, 100_000)
leather_cap = Armor("leather cap", LEATHER_CAP_DESC, "HE", 0.03, 15)
scale_mittens = Armor("scale mittens", SCALE_MITTENS_DESC, "HA", 0.02, 18)
hunting_boots = Armor("hunting boots", HUNTING_BOOTS_DESC, "F", 0.05, 25)

# Items.
lab_key = MiscItem("large key", "A hefty brass key", 1)
storage_key = MiscItem("small key", "A peculiar iron key.", 1)
small_health_potion = Potion("small health potion", SMALL_HEALTH_POTION_DESC, 8, 10)
medium_health_potion = Potion("medium health potion", MEDIUM_HEALTH_POTION_DESC, 18, 25)
large_health_potion = Potion("large health potion", LARGE_HEALTH_POTION_DESC, 50, 50)
cure_disease_potion = Potion("cure disease potion", CURE_DISEASE_POTION_DESC, 35, 0, "yes")

# NPCs/Enemies.
necromancer_npc = NPC("necromancer")
gay_rat_npc = NPC("gil")

gay_rat_enemy = Enemy("gil", 2.00, [10, 20], 99, 0.50, GIANT_RAT_INTRO_DESC, GAY_RAT_DEATH_DESC, 100, 1000, gay_rat_npc, False)
giant_rat = Enemy("giant rat", 12.00, [4, 8], 5, 0.25, GIANT_RAT_INTRO_DESC, GIANT_RAT_DEATH_DESC, 7, 100)
wraith = Enemy("wraith", 25.00, [6, 13], 5, 0.25, WRAITH_INTRO_DESC, WRAITH_DEATH_DESC, 12, 200)
ghoul = Enemy("ghoul", 40.00, [9, 15], 5, 0.25, GHOUL_INTRO_DESC, GHOUL_DEATH_DESC, 23, 500)
skeleton = Enemy("skeleton", 30.00, [7, 12], 5, 0.25, SKELETON_INTRO_DESC, SKELETON_DEATH_DESC, 20, 350)
necromancer = Enemy("necromancer", 75.00, [14, 20], 10, 0.30, NECROMANCER_INTRO_DESC, NECROMANCER_DEATH_DESC, 100, 1000, necromancer_npc, False)
