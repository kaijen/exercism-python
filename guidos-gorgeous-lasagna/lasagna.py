"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate preparation time depending on number of layers

    :param number_of_layers: int - baking time already elapsed.
    :return: int - remaining preparation time (in minutes) derived from 'PREPARATION_TIME_PER_LAYER'.

    Function that takes the actual number of layers and returns how many minutes the lasagna
    needs for preparation based on `PREPERATION_TIME_PER_LAYER`
    """

    return PREPARATION_TIME_PER_LAYER * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate preparation time depending on number of layers

    :param number_of_layers: int - baking time already elapsed.
    :param elapsed_bake_time: int -
    :return: int - remaining preparation time (in minutes) derived from 'PREPARATION_TIME_PER_LAYER'.

    Function that returns the total number of minutes the lasagna has been cooking,
    or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
