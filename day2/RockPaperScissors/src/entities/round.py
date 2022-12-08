class Round:
    def __init__(self, attack: str, counter_attack: str):
        self.__attack: str = attack
        self.__counter_attack: str = counter_attack
        self.__shape_score: dict = {
            'X': 1,
            'Y': 2,
            'Z': 3
        }
        self.__score_rules: dict = {
            ('A', 'Z'): 0,
            ('B', 'X'): 0,
            ('C', 'Y'): 0,
            ('A', 'X'): 3,
            ('B', 'Y'): 3,
            ('C', 'Z'): 3,
            ('A', 'Y'): 6,
            ('B', 'Z'): 6,
            ('C', 'X'): 6
        }
        self.__response_rules: dict = {
            ('A', 'X'): 'Z',
            ('B', 'X'): 'X',
            ('C', 'X'): 'Y',
            ('A', 'Y'): 'X',
            ('B', 'Y'): 'Y',
            ('C', 'Y'): 'Z',
            ('A', 'Z'): 'Y',
            ('B', 'Z'): 'Z',
            ('C', 'Z'): 'X'
        }

    @property
    def attack(self) -> str:
        return self.__attack

    @property
    def counter_attack(self) -> str:
        return self.__counter_attack

    @property
    def score(self) -> int:
        return self.__shape_score[self.__counter_attack] + self.__score_rules[(self.__attack, self.__counter_attack)]

    @property
    def response(self) -> int:
        response = self.__response_rules[self.__attack, self.__counter_attack]
        return self.__shape_score[response] + self.__score_rules[(self.__attack, response)]

    def __str__(self):
        return f"{(self.__attack, self.__counter_attack)} -> score({self.score}), response({self.response})"

    def __repr__(self):
        return str(self)
