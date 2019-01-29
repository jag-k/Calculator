from params import *


def shift(args):
    if args[-1] + 1 >= len(ACTIONS):
        return shift(args[:-1]) + [0]
    args[-1] += 1
    return args


sets = [0] * MOVES
for j in range(len(ACTIONS) * MOVES):
    res = START
    for action in map(lambda x: ACTIONS[x], sets):
        try:
            res = action(res)
        except Exception:
            pass

    if res == GOAL:
        break
    sets = shift(sets)

print(*map(lambda x: ACTIONS[x].__doc__, sets), sep="\n")
