from params import *
print("Current Level: ", current_level)


def shift(args):
    if args[-1] + 1 >= len(ACTIONS):
        return shift(args[:-1]) + [0]
    args[-1] += 1
    return args


sets = [0] * MOVES
for j in range(len(ACTIONS) ** MOVES):
    res = START
    error = False

    for action in map(lambda x: ACTIONS[x], sets):
        try:
            res = action(res)
        except Exception:
            error = True
            break

    # print(j, sets, res)
    if error:
        sets = shift(sets)
        continue

    if res == GOAL:
        print("\nSOLUTION FOUND!", end='')
        break
    sets = shift(sets)

print("\x1b[32m", *map(lambda x: ACTIONS[x].__doc__, sets), sep="\x1b[0m\n\x1b[32m", end="\x1b[0m")
