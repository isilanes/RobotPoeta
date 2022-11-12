import copy
import random
from typing import Optional


STRINGS = {
    1: {
        "str": "hablando con",
        "next": [2, 4, 6, 7, 9, 12, 13, 17],
    },
    2: {
        "str": "inmigrantes",
        "next": [3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    3: {
        "str": "agonizaron durante",
        "next": [4, 13],
    },
    4: {
        "str": "las revelaciones",
        "next": [3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    5: {
        "str": "me sorprende ver",
        "next": [1, 2, 4, 6, 8, 9, 12, 13, 17],
    },
    6: {
        "str": "un bosque para",
        "next": [2, 4, 7, 8, 9, 12, 13, 17],
    },
    7: {
        "str": "nosotros",
        "next": [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    8: {
        "str": "cuando tu",
        "next": [9, 12],
    },
    9: {
        "str": "belleza especial",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    10: {
        "str": "e incluso la intuición",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    11: {
        "str": "apabulla con su",
        "next": [9, 12],
    },
    12: {
        "str": "corte y",
        "next": [3, 7, 9, 13, 14, 15, 16, 17, 18],
    },
    13: {
        "str": "hervideros de ideas",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18],
    },
    14: {
        "str": "ahora es mi momento",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18],
    },
    15: {
        "str": "le voy a poner",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18],
    },
    16: {
        "str": "piden más",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 18],
    },
    17: {
        "str": "botellas de cristal",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18],
    },
    18: {
        "str": "sean normales",
        "next": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17],
    },
}


class Poema:

    def __init__(self, config):
        self.config = copy.deepcopy(config)
        self._left = list(self.config.keys())
        self._output = []

    def next_step(self, i: int) -> Optional[int]:
        available = self.config.get(i).get("next")
        
        if not available:
            return None

        n = random.choice(available)

        # Add current choice to output:
        self._output.append(self.config.get(n).get("str"))

        # Remove current choice from future choices:
        for v in self.config.values():
            if n in v["next"]:
                v["next"].remove(n)

        # Remove current choice from choices left:
        self._left.remove(n)

        return n

    def run(self) -> None:
        i = random.choice(self._left)

        while self._left:
            i = self.next_step(i)

            if i is None:
                break

        print(" ".join(self._output))


def main():
    poema = Poema(STRINGS)
    poema.run()


if __name__ == "__main__":
    main()
