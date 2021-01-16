"""
Map layout.

Large dictionary to keep values for each room.
"""

from configparser import ConfigParser

from engine.instances import *

# 80 characters for reference:
#------------------------------------------------------------------------------#
# Room descriptions.


ENTRANCE_DESC = """You are in the entrance place, it's a musty, hallowed out cave that presumably
was once a hangout for bandits and other vandals.

There is a put out cooking spit on the left side of the place surrounded by a
couple wooden tables and their chairs. Over in the corner stands some drawers
and cabinets, a place to stash away whatever armor, trinkets, and valuables they
had 'found' in the world. All but a few of the sacks that once held abundant
food are strewn across the ground empty, with some leaving rotten fruit. Several
withered burlap sleeping bags lay in the corner and have been ridden by cobwebs.
It seems this place has been abandoned long ago.

You see only one door ahead to the east."""


SECOND_DUNGEON_ROOM_DESC = """You are in the second part of the dungeon room, but this time there is
laid-out humanoid corpse on a table in the middle of the room.

It was a grisly sight to be seen, and coming in from the previous room you are
horrified by just how much specimens were taken in for whatever necromantic
experiments this wizard had in mind. The room is brightened up by artificial
orbs, obviously as to inspect each nook and cranny of the corpse as visually
accurately as possible. The body is headless but is otherwise completed with
limbs stitched up from other foreign bodies. Lain in front the table are some
rusty scalpels, forceps, clamps, and other surgical instruments alongside some
notes in a language you've never seen before as well as prepared diagrams
from open books. Knowing who you are dealing with, you hope whatever is on that
table doesn't become undead.

The only door is the one back to the first dungeon room, which is to the east."""


STORAGE_ROOM_DESC = """You are in the storage room.

You see all the chests, crates, cabinets, and drawers that store the belongings
of whoever lives here. However, most of what's in here don't seem to be of any
use to you right now.

The only door is the one back towards the east."""


FAILED_EXPERIMENTS_ROOM_DESC = """You are in the failed experiments room.

Calling it disgusting would be an overwhelming understatement but you manage to
suck it up and stay in the room. At least none of the piles of flesh on the
floor are moving anymore, you hope...

The only door is the one back to the library, which is to the east."""


LESSER_HALL_DESC = """You put away your torchlight as the hall in front of you is already lit up by
their own across stone brick walls and floor.

This place seems cleaner and more lively as if someone regularly comes to
perform upkeep on it. It's not a long hall and there's a single drawer off to
the side with some decor on top.

You see a door to the east at the end of the hallway, with the opposing door to
the west."""


FIRST_DUNGEON_ROOM_DESC = """You enter the dungeon room.

Jail cells line both sides of the wall all through the end of the room, each
separated by a stone brick wall. They don't look like they were meant to be
lived in as only a pile of hay and sometimes a small tray of scraps are found in
each cell. Perhaps the jailer temporarily held them there until they were taken
out for experiments?

There is a door to the west and a door to the north."""


DINING_ROOM_DESC = """You have reached the dining room.

You see the preparation tables and cabinets on the far end as well as a boiling
cauldron of water and a burning cooking spit to the side. There are two dining
tables in the middle of the room, but there doesn't seem to be anyone else
living inside this lair to fulfill it. Perhaps the necromancer likes to conjure
up some undead to feast with?

There is a door to the west, a door to the south, and a door to the east."""


LIBRARY_ROOM_DESC = """You are in the library room.

There are three standing bookshelves on the south side of the room parallel to
each other with enough space between them to pass through. On the other side
of the room is a small reading desk with notes and a lit lantern on top.

There is a door to the west, a larger door to the north, and a door to the east."""


SPELLS_ALCHEMY_LAB_DESC = """You are in the spells and alchemy lab.

It's misty with a tinge of acid in the air that just so subtly burns the insides
of your nose. The floor is damp in most areas so you cautiously maneuver around,
avoiding bumping into any of the busy tables and stands lined from end to end
with various beakers, filled and empty, and the books and scratch notes that
accompany them. The bubbling from the active cauldron and fuzzing from the
tipping of the working beakers fill up the bustling ambience of the room. You
spot a portriat of a woman painted on a miniature canvas on the main desk.

It's almost a shame that you are to put an abrupt stop to this man's life's work
by the time you'll have dealt with him. Remember that by clearing certain,
unique locations like this allow you to pinpoint the whereabouts for a local
guild for which you'd be rewarded influence points and special items.

There is a door to the north and the large door you came from to the south."""

#------------------------------------------------------------------------------#
MASTER_CHAMBER_DESC = """You open the door to reveal... nothing? Two dim, blue flames light up on the
other side of the room but not bright enough to reveal anything else. You step
in to investigate and the door behind you suddenly slams shut as the entire room
is lit up torch by torch all along the walls. You spot the figure responsible
for the sudden performance ahead of you in night black robes with both arms
raised to hold the two blue flames you saw on the palms of his hand, his
menacing grin directed at you."""


SHRINE_ROOM_DESC = """You are in what looks to be a shrine room as in front of
you stands a medium-sized bronze statue of a robed figure propped up on a
pedestal, staring down at you menacingly.

Surrounding it are some unusual plants and on the platform lay various items for
tribute, one of these being a bowl of cracked bones and animal parts. You sense
a faint but dark presence crawling up the hairs of your skin as you edge closer
to the statue and get the feeling the bronze figure represented is somehow
present with you the room.

There's a door leading to the north and a door to the west."""


GREATER_HALL_DESC = """You are in a much bigger hallway, this time the ceiling being arched nicely and
the sides of the walls having wooden support beams with hanging candles.

There's a singular, large painting of a landscape off to the side on the right
and further out are hanging cages with bones inside. Below those is a work table
with books and a quill and parchment.

There's a door towards the north, a door right next to it towards the west, and
a door to the south."""


BOTANY_ROOM_DESC = """You are in the botany room. It's lush with all kinds of plant species in large
pots and gardens, hanging from the ceiling, or off to the sides of the mossy
walls as veins.

The entire room is being lit by artificial floating orbs above, likely used to
keep the plants thriving in lieu of sunlight. In the middle of all of it stands
a long study desk with specimens in jars, plant samples, and glass beakers. A
mini bookshelf and a tubed boiler mechanism accompany it.

There is a door to the west and a door to the south."""

#------------------------------------------------------------------------------#

ROOM_NAME = "ROOM_NAME"
DESC = "DESC"
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

hotspot = "hotspot"  # Room has trap or enemy.
b_trapped = "b_trapped"  # Room is booby trapped.
locked = "locked"  # Room needs a key to open.
passed = "passed"  # Player has already entered room.
examined = "examined"  # Player has already examined room.
items = "items"  # Room contains items.
has_enemy = "has_enemy"  # Room has an enemy.
met_enemy = "met_enemy"  # Player already met enemy in room aftering fleeing.
enemy = "enemy"  # Enemy instance.

room_list = {
    "00": {
        ROOM_NAME: "00",
        DESC: "000000000",
        NORTH: "a1",
        EAST: None,
        SOUTH: None,
        WEST: None,

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "a1": {
        ROOM_NAME: "entrance place",
        DESC: ENTRANCE_DESC,
        NORTH: None,
        EAST: "b1",
        SOUTH: None,
        WEST: None,

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [small_health_potion],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "a2": {
        ROOM_NAME: "second dungeon room",
        DESC: SECOND_DUNGEON_ROOM_DESC,
        NORTH: None,
        EAST: "b2",
        SOUTH: None,
        WEST: None,

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [medium_health_potion, storage_key],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "a3": {
        ROOM_NAME: "storage room",
        DESC: STORAGE_ROOM_DESC,
        NORTH: None,
        EAST: "b3",
        SOUTH: None,
        WEST: None,

        hotspot: False,
        b_trapped: False,
        locked: True,
        passed: False,
        examined: False,
        items: [dlc_armor, cure_disease_potion, lab_key],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "a4": {
        ROOM_NAME: "failed experiments room",
        DESC: FAILED_EXPERIMENTS_ROOM_DESC,
        NORTH: None,
        EAST: "b4",
        SOUTH: None,
        WEST: None,

        hotspot: True,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [chainmail_armor, medium_health_potion],
        has_enemy: True,
        met_enemy: False,
        enemy: ghoul,
        },
    "b1": {
        ROOM_NAME: "lesser hallway",
        DESC: LESSER_HALL_DESC,
        NORTH: None,
        EAST: "c1",
        SOUTH: None,
        WEST: "a1",

        hotspot: True,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [small_health_potion],
        has_enemy: True,
        met_enemy: False,
        enemy: giant_rat,
        },
    "b2": {
        ROOM_NAME: "first dungeon room",
        DESC: FIRST_DUNGEON_ROOM_DESC,
        NORTH: "b3",
        EAST: None,
        SOUTH: None,
        WEST: "a2",

        hotspot: True,
        b_trapped: True,
        locked: False,
        passed: False,
        examined: False,
        items: [leather_cap],
        has_enemy: True,
        met_enemy: False,
        enemy: skeleton,
        },
    "b3": {
        ROOM_NAME: "dining room",
        DESC: DINING_ROOM_DESC,
        NORTH: None,
        EAST: "c2_3",
        SOUTH: "b2",
        WEST: "a3",

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [hunting_boots],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "b4": {
        ROOM_NAME: "library room",
        DESC: LIBRARY_ROOM_DESC,
        NORTH: "b5",
        EAST: "c4",
        SOUTH: None,
        WEST: "a4",

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [fine_steel_sword],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "b5": {
        ROOM_NAME: "spells and alchemy lab",
        DESC: SPELLS_ALCHEMY_LAB_DESC,
        NORTH: "b6",
        EAST: None,
        SOUTH: "b4",
        WEST: None,

        hotspot: False,
        b_trapped: False,
        locked: True,
        passed: False,
        examined: False,
        items: [large_health_potion],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "b6": {
        ROOM_NAME: "master chamber",
        DESC: MASTER_CHAMBER_DESC,
        NORTH: None,
        EAST: None,
        SOUTH: "b5",
        WEST: None,

        hotspot: True,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [],
        has_enemy: True,
        met_enemy: False,
        enemy: necromancer
        },
    "c1": {
        ROOM_NAME: "shrine room",
        DESC: SHRINE_ROOM_DESC,
        NORTH: "c2_3",
        EAST: None,
        SOUTH: None,
        WEST: "b1",

        hotspot: False,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    "c2_3": {
        ROOM_NAME: "greater hallway",
        DESC: GREATER_HALL_DESC,
        NORTH: "c4",
        EAST: None,
        SOUTH: "c1",
        WEST: "b3",

        hotspot: True,
        b_trapped: False,
        locked: False,
        passed: False,
        examined: False,
        items: [medium_health_potion, scale_mittens],
        has_enemy: True,
        met_enemy: False,
        enemy: wraith,
        },
    "c4": {
        ROOM_NAME: "botany room",
        DESC: BOTANY_ROOM_DESC,
        NORTH: None,
        EAST: None,
        SOUTH: "c2_3",
        WEST: "b4",

        hotspot: False,
        b_trapped: True,
        locked: False,
        passed: False,
        examined: False,
        items: [small_health_potion],
        has_enemy: False,
        met_enemy: False,
        enemy: None,
        },
    }

#------------------------------------------------------------------------------#

# OPTIONALS IN CONFIG
config = ConfigParser()
ini_file = "engine/data/config.ini"
config.read(ini_file)
disable_enemies = config.getboolean("Other", "disable_enemies")
disable_traps = config.getboolean("Other", "disable_traps")

# Disables enemies if True in config,
# also doesn't get rid of necromancer.
if disable_enemies is True:
    for room, dict in room_list.items():
        for name, value in dict.items():
            if dict[enemy] != necromancer:
                dict[enemy] = None
                dict[has_enemy] = False
            dict[hotspot] = False
    print("Disabled enemies")

# Disables traps if True in config
if disable_traps is True:
    for room, dict in room_list.items():
        for name, value in dict.items():
            dict[b_trapped] = False
            dict[hotspot] = False
    print("Disabled traps")
