
class Team(object):

    def __init__(self, team_name, formation, manager_name, goalie, player_list, player_dict):

        self.team_name = team_name
        self.formation = formation
        self.manager_name = manager_name
        self.goalie = goalie
        self.player_list = player_list
        self.player_dict = player_dict

    def get_team_name(self):

        return self.team_name

    def get_formation(self):

        return self.formation

    def get_manager_name(self):

        return self.manager_name

    def get_goalie_name(self):

        return self.goalie[0]

    def get_goalie_number(self):

        return self.goalie[1]

    def get_goalie_country(self):

        return self.goalie[2]

    def get_player_list(self):

        return self.player_list

    def get_player_by_number(self, jersey_number):

        return self.player_dict[jersey_number]

    def get_player_indexed(self, index):

        return self.player_list[index]


# Below is prompting the user to input data about teams

global everton
global brighton

num_teams = input("How many teams are we using? ")

for team_index in range(int(num_teams)):

    goalie = []
    player_list = []
    player_dict = {}

    team_name = input("Enter team name: ")
    formation = input("Enter formation: ")
    manager_name = input("Enter manager name: ")
    goalie.append(input("Enter goalie name: "))
    goalie.append(input("Enter goalie jersey number: "))
    goalie.append(input("Enter goalie country: "))

    number_players = input("How many players on the field? ")
    for player_index in range(int(number_players)):

        player_details = []
        player_dict_temp = {}

        player_name = input("Enter player name: ")
        player_jersey_number = input("Enter player jersey number: ")
        player_country = input("Enter player country: ")

        player_details.append(player_name)
        player_details.append(player_jersey_number)
        player_details.append(player_country)

        player_dict[player_jersey_number] = player_details
        player_dict_temp[player_jersey_number] = player_details

        player_list.append(player_dict_temp)

    print(player_list)
    print(player_dict)
    print(team_name)

    if team_name == "Everton":

        print("Adding to everton")
        everton = Team(team_name, formation, manager_name, goalie, player_list, player_dict)

    elif team_name == "Brighton":

        print("Adding to brighton")
        brighton = Team(team_name, formation, manager_name, goalie, player_list, player_dict)


def print_formations():

    if everton.formation == "4 4 2":

        print(everton.team_name, "formation:")

        print('\t\t\t   ', everton.get_goalie_name())

        print(everton.get_player_by_number('19')[0], '\t', everton.get_player_by_number('4')[0], '\t',
              everton.get_player_by_number('2')[0], '\t', everton.get_player_by_number('12')[0])

        print()

        print(everton.get_player_by_number('11')[0], '\t', everton.get_player_by_number('10')[0], '\t',
              everton.get_player_by_number('26')[0], '\t', everton.get_player_by_number('20')[0])

        print()

        print('\t', everton.get_player_by_number('7')[0], '\t', everton.get_player_by_number('9')[0])

        print()

    if brighton.formation == " 3 4 3":

        print("Brighton formation:")

        print('\t\t', brighton.get_goalie_name())

        print(brighton.get_player_by_number('15')[0], '\t', brighton.get_player_by_number('5')[0], '\t',
              brighton.get_player_by_number('4')[0])

        print()

        print(brighton.get_player_by_number('22')[0], '\t', brighton.get_player_by_number('6')[0], '\t',
              brighton.get_player_by_number('24')[0], '\t', brighton.get_player_by_number('30')[0])

        print()

        print(brighton.get_player_by_number('16')[0], '\t', brighton.get_player_by_number('7')[0], '\t',
              brighton.get_player_by_number('11')[0])

        print()

def print_first_part():

    print(everton.get_player_by_number('7')[0], "passes to", everton.get_player_by_number('20')[0], ',',
          everton.get_player_by_number('20')[0], "passes to", everton.get_player_by_number('12')[0], ',',
          everton.get_player_by_number('12')[0], "passes to", everton.get_player_by_number('7')[0], ',',
          everton.get_player_by_number('7')[0], "shoots it into the goal and scores!")


def print_second_part():

    print(brighton.get_player_by_number('16')[0], "passes the ball to", brighton.get_player_by_number('7')[0], ',',
          brighton.get_player_by_number('7')[0],
          "passes the ball to #17 Glenn Murray and hits the ball with the outside of his foot barely missing the goal")

print_formations()
print_first_part()







