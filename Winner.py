from Rules import Rules


class Winner:

    rules = Rules("poker")

    def __init__(self, name):
        self.name = name

    def check_high_card(self, hand, hand2, flop):
        player_1_hc = self.rules.high_card(hand, flop)
        player_2_hc = self.rules.high_card(hand2, flop)

        player_1_hc.sort(), player_2_hc.sort()
        winner = ""

        if player_1_hc[1] > player_2_hc[1]:
            winner = "p1"
        elif player_1_hc[1] < player_2_hc[1]:
            winner = "p2"
        elif player_1_hc[1] == player_2_hc[1]:
            if player_1_hc[0] > player_2_hc[0]:
                winner = "p1"
            elif player_1_hc[0] < player_2_hc[0]:
                winner = "p2"
            else:
                winner = "split"
        return winner

    def check_pairs(self, hand_p1, hand_p2, flop):
        winner = ""
        pairs_dict = {
            "": 0, "pair": 1, "two pair": 2, "three of a kind": 3,
            "full house": 4, "four of a kind": 5
        }

        result1 = self.rules.pairs(hand_p1, flop)
        result2 = self.rules.pairs(hand_p2, flop)

        print(result1)
        print(result2)

        value1 = pairs_dict[result1[0][0]]
        value2 = pairs_dict[result2[0][0]]

        if value1 > value2:
            winner = "p1"
        elif value1 < value2:
            winner = "p2"
        else:
            pass


