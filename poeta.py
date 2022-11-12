import copy
import random
from typing import Optional


STRINGS = {
    1: {
        "str": "hablando con",
        "next": [2],
    },
    2: {
        "str": "inmigrantes",
        "next": [],
    },
    3: {
        "str": "agonizaron durante",
        "next": [4],
    },
    4: {
        "str": "las revelaciones",
        "next": [5],
    },
    5: {
        "str": "me sorprende ver",
        "next": [6],
    },
    6: {
        "str": "un bosque para",
        "next": [7],
    },
    7: {
        "str": "nosotros",
        "next": [8],
    },
    8: {
        "str": "cuando tu",
        "next": [9],
    },
    9: {
        "str": "belleza especial",
        "next": [10],
    },
    10: {
        "str": "e incluso la intuición",
        "next": [11],
    },
    11: {
        "str": "apabulla con su",
        "next": [12],
    },
    12: {
        "str": "corte y",
        "next": [13],
    },
    13: {
        "str": "hervidero de ideas",
        "next": [14],
    },
    14: {
        "str": "ahora es mi momento",
        "next": [15],
    },
    15: {
        "str": "le voy a poner",
        "next": [16],
    },
    16: {
        "str": "piden más",
        "next": [17],
    },
    17: {
        "str": "botellas de cristal",
        "next": [18],
    },
    18: {
        "str": "sean normales",
        "next": [],
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
