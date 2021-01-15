"""
Typewriter effect to display text.
"""

import sys
import os
import time


def type(text: str, interval1=0.04, interval2=0.75) -> None:
    """
    Input: Desired message called as argument (1st parameter). Slower default interval,
    0.04 seconds (2nd parameter). Faster interval, 0.75 second (3rd parameter).
    ---
    Output: Message but now with cool typewriter effect.
    """

    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()

        # If text has any punctuation from list, make time interval longer.
        pauses = [".", ",", "?", "!", ":"]
        if i in pauses:
            time.sleep(interval2)
        else:
            time.sleep(interval1)
