"""Practicing utility functions for dictionaries."""

__author__: str = "730530237"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of a given dictionary."""
    result: dict[str, str] = {}
    for key in dictionary:
        check: str = dictionary[key]  # check if it already exists - comes first!!
        if check in result:  # check to see if a value is in a dict
            raise KeyError(
                "Dictionary values cannot repeat for the invert function to work!"
            )
        result[dictionary[key]] = (
            key  # if nonexistent, add a new key-value pair to result
        )
    return result


# this one took me a while, so I made lots of comments LOL
def favorite_color(inp: dict[str, str]) -> str:
    """This function finds and returns the most popular favorite color in a dict."""
    colors: dict[str, int] = {}  # this will store each color and its count
    for key in inp:
        if inp[key] in colors:  # if the color is already in the list
            colors[inp[key]] += 1  # then add the count
        else:
            colors[inp[key]] = 1  # if not, start at 1
    fav_color: str = ""
    color_count: list[int] = []  # track instances of each color
    current_count: int = 0  # tracker
    max_count: int = 0  # max number of votes
    for option in colors:  # now iterate thru list of color: instances
        current_count = colors[option]
        if current_count > max_count:  # like high card example
            if (
                colors[option] not in color_count
            ):  # make sure if equal votes, first color gets it
                color_count.append(
                    colors[option]
                )  # add the number of votes to the list
                max_count = current_count
                fav_color = option
    return fav_color


def count(inp: list[str]) -> dict[str, int]:
    """Takes a list of str and returns dict of str: instances"""
    result: dict[str, int] = {}
    for x in inp:
        if x in result:  # if it already exists
            result[x] += 1  # add one
        else:
            result[x] = 1  # similar to the above function
    return result


def alphabetizer(inp: list[str]) -> dict[str, list[str]]:
    """Turn list into keys of one letter and values of each first-letter word."""
    result: dict[str, list[str]] = {}
    for strings in inp:
        letter: str = strings[0].lower()  # make them all lowercase
        if letter in result:
            result[letter] += [strings]  # adding to the values list at letter key
        else:
            result[letter] = [
                strings
            ]  # starting off letter key by adding to the values list
    return result


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Update an existing attendance log with new days and students"""
    if day in log:
        log[day] += [student]  # add that student to value list
    else:
        log[day] = [
            student
        ]  # same construct as above, either add to or begin day key-value pair
