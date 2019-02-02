from actions import *

GOAL = START = MOVES = 0
ACTIONS = []
current_level = 13


def level_36():
    global GOAL, START, MOVES, ACTIONS
    GOAL = -85
    START = 0
    MOVES = 4

    ACTIONS = [
        addition(6),
        concat(5),
        addition(-7)
    ]


def level_2():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 8
    START = 0
    MOVES = 3

    ACTIONS = [
        addition(2),
        addition(3)
    ]


def level_3():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 12
    START = 0
    MOVES = 3

    ACTIONS = [
        addition(2),
        addition(1),
        multiplication(4)
    ]

# LEVEL 5 ERROR


def level_7():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 5
    START = 4
    MOVES = 3

    ACTIONS = [
        addition(3),
        multiplication(3),
        division(3)
    ]


def level_9():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 4
    START = 0
    MOVES = 3

    ACTIONS = [
        addition(8),
        multiplication(5),
        delete(),
    ]


def level_10():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 9
    START = 50
    MOVES = 4

    ACTIONS = [
        division(5),
        multiplication(3),
        delete(),
    ]


def level_11():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 100
    START = 99
    MOVES = 3

    ACTIONS = [
        addition(-8),
        multiplication(11),
        delete(),
    ]


def level_13():
    global GOAL, START, MOVES, ACTIONS
    GOAL = 23
    START = 171
    MOVES = 4

    ACTIONS = [
        addition(-9),
        multiplication(2),
        delete(),
    ]


if "level_" + str(current_level) not in dir():
    current_level = int((
        max(filter(lambda x: x.startswith('level_'), dir()), key=lambda x: int(x.split('_', 1)[1]))).split("_", 1)[1]
    )

eval(f"level_{current_level}()")
