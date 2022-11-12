import copy
import random


STRINGS = {
    1: {
        "str": "hablando con",
        "next": [1, 2],
    },
    2: {
        "str": "inmigrantes",
        "next": [1, 2],
    }
}


class Poema:

    def __init__(self, config):
        self.config = copy.deepcopy(config)
        self._left = list(self.config.keys())

    def current(self):
        c = random.choice(self._left)
        for v in self.config.values():
            v["next"].remove(c)

        return c


def main():
    poema = Poema(STRINGS)

    current = poema.current()

    print(poema.config)

    return

    output = []
    while left:
        available = STRINGS.get(current).get("next")
        if not available:
            break



if __name__ == "__main__":
    main()
