"""
Intro sequence
Get name and initiate player instance
"""

import os
import textwrap
from time import sleep

from engine.instances import my_player
from engine.classes import Player
from engine.typewriter import *

def intro_sequence() -> None:
    """Welcomes the user, gets name, and plays story intro if user wants."""

    global my_player

    os.system("cls")
    type("Welcome to...", 0.04, 0.04)
    sleep(1.5)
    print("""
  _____       _          _____ _              __       _      
  \_   \_ __ | |_ ___   /__   \ |__   ___    / /  __ _(_)_ __ 
   / /\/ '_ \| __/ _ \    / /\/ '_ \ / _ \  / /  / _` | | '__|
/\/ /_ | | | | || (_) |  / /  | | | |  __/ / /__| (_| | | |   
\____/ |_| |_|\__\___/   \/   |_| |_|\___| \____/\__,_|_|_|
""")
    sleep(1)
    type("A roguelike, text-based RPG", 0.04, 0.1)
    sleep(1)
    type("\nEnter 'quit' in-game to exit program")
    type("\nHave fun!\n\nStart game? (Y/N)\n")

    while True:  # Loop for valid input.
        start = input("> ").lower().strip()

        if start == "y":
            break
        elif start == "n":
            sys.exit()
        else:
            print("\nInvalid input")

    intro_text = [
            '"This must be it," you think to yourself as you wade your torch in front of you and step in to reveal a dimly lit cavernous opening. A couple torches on the other side by a door mark a passageway deeper into the mountain. On your other hand, you grip the handle of your blade strapped onto your belt, waiting for any opportune attacks from whatever or whoever lurks in these dark and misty shafts.',
            "You had been tasked by the town bailiff, Randolf Flintler, to deal with the necromancer who's been terrorizing the people of Stennerden for weeks on end, especially towards the bailiff and his manor. A few of the town's guards had also been tasked with the same job, but either one group never came back or had no luck in finding the dark mage's whereabouts. You weren't sure why the town was targeted or what even caused it; all you know is that a large bounty of aurels is waiting for you by the time you get back.",
            "But you heard from some helpful wanderers and locals about the mysterious lights and sounds and grimly undead to have come out of this one particular area. You treaded down the old path towards Findale up until you reached the second stream crossing, then made a right at the short waterfall and eventually reached the old and abandoned iron mine.",
            "And that's where you are now..."
        ]

    os.system("cls")
    type("\nGreetings adventurer! What is your name?\n")
    while True:  # Loop to get player name.
        your_name = input("> ").strip()

        confirmed = input(f"\nConfirm name? (Y/N): {your_name.title()}\n> ").strip().lower()
        if confirmed == "y":
            my_player.name = your_name.title()  # Stores player name once confirmed.
            break
        elif confirmed == "n":
            print("\nWhat is your name?")
            continue
        else:
            print("\nInvalid input")

    # User chooses to skip story intro or not.
    type("\nSkip story intro? (Y/N)\n", 0.04, 0.3)
    while True:
        skip = input("> ").strip().lower()

        if skip == "y":
            return
        elif skip == "n":
            break
        else:
            print("\nInvalid input")

    # Display each intro text line if user does not skip.
    os.system("cls")
    type("Prologue...", 0.04, 0.5)
    sleep(2)
    os.system("cls")
    for section in intro_text:
         print()
         type(textwrap.fill(section, 80))
         input("\n\n...")
         os.system("cls")
