"""
Ending sequence: final text for storyline
"""

import os
import textwrap
from time import sleep
from engine.typewriter import *
from engine.instances import my_player


def ending_sequence(ending: int) -> None:
    """
    ending: 0) Player has slain the necromancer, but is blissfully unaware of the
               truth that reside in Stennerden.

    ending: 1) After learning the truth from the necromancer, Player never gave
               in to his manipulative words, and slays him in the end.

    ending: 2) Player is convinced and seeks to aid the necromancer after the truth
               has been revealed.
    """

    os.system("cls")

    ending_dict = {
        0: [
            "Your epic battle against the necromancer ends in a prideful victory. But the lair died along with him, and everything went dark.",
            "So you light up a torch and find your way outside undisturbed.",
            "As you travel back to town, you wonder about the motives of the necromancer. Perhaps you could have stayed a while longer and inquired more?",
            "But your steadfast and unquestioning attitude had only cared about completing the job.",
            "Which makes for good mercenaries.",
            "But that doesn't matter anymore. What's important is that the deed is done and your fat sack of aurels is minutes away....",
            ],

        1: [
            "In the end, you never gave in to his words. This threat to the world has been eliminated and you feel a sense of pride after accomplishing such a feat.",
            "But the lair went dark shortly after his last breath. His lifesoul is attached to the magic that light up the rooms it seems.",
            "But no worries, you light up a torch and find your way outside undisturbed.",
            "As you travel back to town, you wonder how might you confront the bailiff after hearing about the truth.",
            f'"Thank you, {my_player.name}, for you have done me and the town a great service," Randolf shows you his gratitude as he hands you your reward.',
            "But you only look at him dead straight in the eyes with contempt....",
            ],

        2: [
            "With your newfound ally and master, your fervor and intense curiosity burns with great passion over the wonders of new powers that you will behold.",
            "Together, a dauntless warrior with a mastermind necromancer shall rise up from the ashes and fear will reign over that defy them, you fantasize.",
            "But the plan at hand is to capture the bailiff and bring him to Nightcaster.",
            "You wonder what might happen to Randolf once he is captured, and if after all these years it was even worth it anymore.",
            "But the necromancer refused to tell a single detail about it.",
            "And so commences the plan one late evening as you set out for the town, his menacing laughs behind your shoulder.",
            "At the perfect hour and at the perfect place, the bailiff oblivious of the last few minutes of his normal life coming to an end, it was too good to turn back.",
            "And that was the last time he ever set foot in the town....",
            ],
        }

    # Displays each line one at a time.
    for section in ending_dict[ending]:
        print()
        type(textwrap.fill(section, 80))
        input("\n\n...")
        os.system("cls")

    type("\nTo be continued..?", 0.04, 0.50)
    sleep(3)

    return
