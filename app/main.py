from math import fabs


class Deck:
    def __init__(self, row, column, is_alive=True):
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start, end, is_drowned=False):
        self.decks = []
        if start[0] == end[0]:
            for i in range(start[1], end[1] + 1):
                self.decks.append(Deck(start[0], i))
        self.start = start
        self.end = end
        self.is_drowned = is_drowned

    def get_deck(self, row, column):
        for deck in self.decks:
            if row == deck.row and column == deck.column:
                return deck
        return None

    def fire(self, row, column):
        for deck in self.decks:
            if row == deck.row and column == deck.column:
                deck.is_alive = False
                if not any([deck.is_alive for deck in self.decks]):
                    self.is_drowned = True
                    return "Sunk!"
                else:
                    return "Hit!"


class Battleship:
    def __init__(self, ships):
        self.ships = []
        if self._validate_field(ships):
            for ship in ships:
                self.ships.append(Ship(start=ship[0], end=ship[1]))

    @staticmethod
    def _validate_field(ships):
        count = 0
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        if len(ships) == 10:
            for ship in ships:
                for j in ships:
                    if j == ship:
                        count += 1
                        continue
                    if ship[0][0] == ship[0][1] == j[0][0] == j[0][1] and fabs(ship[1][1] - j[0][1]) < 2:
                        return False
                    if ship[0][1] == ship[1][1] == j[0][1] == j[1][1] and fabs(ship[1][0] - j[0][0]) < 2:
                        return False
                    if (ship[1][1] == j[0][1] + 1 or ship[1][1] == j[0][1] - 1) and (ship[1][0] == j[0][0] - 1):
                        return False

                if ship[0][0] == ship[1][0] or ship[0][1] == ship[1][1]:
                    x = ship[0][0] - ship[1][0]
                    y = ship[0][1] - ship[1][1]
                    length = fabs(y + x)
                    if length == 3:
                        count_4 += 1
                    if length == 2:
                        count_3 += 1
                    if length == 1:
                        count_2 += 1
                    if length == 0:
                        count_1 += 1
                else:
                    return False

            if count != 10:
                return False

            if count_4 == 1 and count_3 == 2 and count_2 == 3 and count_1 == 4:
                return True
            else:
                return False
        else:
            return False

    def fire(self, location: tuple):
        for ship in self.ships:
            for deck in ship.decks:
                if deck.row == location[0] and deck.column == location[1]:
                    return ship.fire(*location)
        return "Miss!"
