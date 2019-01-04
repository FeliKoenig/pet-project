#from getpass import getpass
from easygui import passwordbox

dict_cat_opt = {"Totally lazy": ["Couchpotato", "Wellness", "Cinema"],
                "Slightly active": ["Meet friends", "Restaurant", "Bar"],
                "Going crazy": ["Barhopping", "Club", "Clubhopping"]}


class Player:
    """
        A class representing a player
    """

    def __init__(self, name):
        self.name = name
        self.category = ""
        self.option = ""

    def choose_category(self):
        category = input("Choose your preferred category: ")
        self.category = [*dict_cat_opt][int(category)-1]



class RPS:
    """
        Game rock, paper, scissors!
    """

    def __init__(self, list_of_players):
        self.list_of_players = list_of_players
        self.options = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        self.message = {"tie": "\nYawn it's a tie! Let\'s play again!",
                        "decision": "\nYay {}, you won! Sorry {}, maybe next time..."}

    def decide_winner(self, rps_choices):

        for i in self.list_of_players:
            print("\n{}, you selected: {}".format(i, rps_choices[i]))

        i = self.list_of_players[0]
        j = self.list_of_players[1]

        if rps_choices[i] == rps_choices[j]:
            print(self.message["tie"])
            return 0
        elif (rps_choices[i] == self.options["R"] and rps_choices[j] == self.options["S"])\
                or (rps_choices[i] == self.options["P"] and rps_choices[j] == self.options["R"])\
                or (rps_choices[i] == self.options["S"] and rps_choices[j] == self.options["P"]):
            print(self.message["decision"].format(i, j))
            return i
        else:
            print(self.message["decision"].format(j, i))
            return j

    def play_RPS(self):
        rps_choices = {}
        for i in self.list_of_players:
            players_rps_choice = passwordbox("{}, please enter Rock (R), Paper (P) or Scissors (S): ".format(i))
            players_rps_choice = self.options[players_rps_choice.upper()]
            rps_choices[i] = players_rps_choice
        winner = self.decide_winner(rps_choices)
        return winner

# function to decide the category
def decide_category(players_categories):
    cat_list = list(players_categories.values())
    list_of_players = list(players_categories.keys())
    if cat_list[0] == cat_list[1]:
        chosen_category = cat_list[0]
        print("\nYou\'ve chosen the same category: {}".format(chosen_category))
    else:
        print("\nYou\'ve chosen different categories: {} and {} "
              "\nLet\'s play Rock, Paper or Scissors to decide.\n".format(cat_list[0], cat_list[1]))
        winner = RPS(list_of_players).play_RPS()
        if winner == 0:
            winner = RPS(list_of_players).play_RPS()
        chosen_category = players_categories[winner]
    return chosen_category


# function to get and store the category choice
def choose_categories(list_of_players):
    players_categories={}
    for i in list_of_players:
        print("\n{}, in which mood are you today? (1) {}, (2) {} or (3) {}"
              .format(i.name, [*dict_cat_opt][0], [*dict_cat_opt][1], [*dict_cat_opt][2]))
        i.choose_category()
        players_categories[i.name] = i.category
    return players_categories


# function to set the players
def set_players():
    player1 = input("Name of Player 1: ")
    player1 = Player(player1)
    player2 = input("Name of Player 2: ")
    player2 = Player(player2)
    return [player1, player2]


if __name__ == '__main__':
    list_of_players = set_players()
    players_categories = choose_categories(list_of_players)
    category = decide_category(players_categories)

