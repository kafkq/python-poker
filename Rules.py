from Cards import Cards


class Rules(Cards):
    cards = Cards("Builder", "Rules")

    value_disct = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
        "K": 13, "A": 14}

    def __init__(self, game):
        self.game = game

    # sequence is either the hand or the flop, index is the number of the card
    def convert_val(self, sequence, index):
        value = self.value_disct[sequence[index].number]
        return value

    @staticmethod
    def convert_symbol(sequence, index):
        value = sequence[index].symbol
        return value

    # list method for easier work
    def list_method(self, list_input):
        list_output = []

        if len(list_input) == 2:
            for index in range(2):
                # we append the values of the cards in a list
                value1 = self.convert_val(list_input, index)
                list_output.append(value1)
        elif len(list_input) == 5:
            for index in range(5):
                # we append the values of the flop in a list
                value = self.convert_val(list_input, index)
                list_output.append(value)

        list_output.sort()
        return list_output

    # rules for the game
    def high_card(self, hand, flop):
        list_output = []
        hand = self.list_method(hand)
        flop = self.list_method(flop)
        combined_list = hand + flop
        combined_list.sort()
        list_output.append(combined_list[-1])
        list_output.append(combined_list[-2])
        return list_output

    def pairs(self, hand, flop):
        hand = self.list_method(hand)
        flop = self.list_method(flop)
        combined_list = hand + flop

        def get_list(list_input):
            item_count = 1
            list_pairs = []
            for item in list_input:
                if item_count == 7:
                    break
                if item == list_input[item_count]:
                    list_pairs.append(item)
                item_count += 1
            return list_pairs

        list_pairs = get_list(combined_list)

        def pairs_check(list_input):
            filter_cards = []
            result = ""
            if len(list_input) == 1:
                result = "pair"
            elif len(list_input) == 2 and list_input[0] != list_input[1]:
                result = "two pair"
            elif len(list_input) == 2 and list_input[0] == list_input[1]:
                result = "three of a kind"
            elif len(list_input) == 3 and list_input[0] == list_input[1] != list_input[2] or\
                    len(list_input) == 3 and list_input[0] != list_input[1] == list_input[2]:
                result = "full house"
            elif len(list_input) == 3 and list_input[0] == list_input[1] == list_input[2]:
                result = "full house"
            # Special cases
            elif len(list_input) == 3 and list_input[0] != list_input[1] != list_input[2]:
                filter_cards.append(list_input[-0]), filter_cards.append(list_input[-1])
                result = "four of a kind"
            return result, list_input

        pairs = pairs_check(list_pairs)
        return pairs, list_pairs

    def straight(self, hand, flop):
        hand = self.list_method(hand)
        flop = self.list_method(flop)

        combined_list = hand + flop
        combined_list.sort()

        straight_set = set(combined_list)
        straight_list = list(straight_set)

        def straight_checker(list_input):
            count = 1
            list_of_values = []
            for index in list_input:
                if count == len(list_input):
                    break
                elif list_input[count] - index == 1:
                    list_of_values.append(index)
                count += 1
                if len(list_of_values) == 4 and list_of_values[3] - list_of_values[0] == 3:
                    return True

        straight_result = straight_checker(straight_list)
        return straight_result

    def flush(self, hand, flop):
        flush_checker = []
        combined_list = hand + flop

        def sym_list_add(list_input):
            combined_list_sym = []
            for index in range(7):
                combined_list_sym.append(self.convert_symbol(list_input, index))
            return combined_list_sym

        def sym_count(list_input):
            # checks for flushes *change the name of the function
            sym = ("♣", "♦", "♥", "♠")
            flush = False
            for x in range(len(sym)):
                count = 0
                for y in range(len(list_input)):
                    if sym[x] == list_input[y]:
                        count += 1
                    if count >= 5:
                        flush = True
            return flush

        combined_sym = sym_list_add(combined_list)
        result = sym_count(combined_sym)
        return result

    def straight_flush(self, hand, flop):
        flush = self.flush(hand, flop)
        straight = self.straight(hand, flop)

        if flush == True and straight == True:
            return True












