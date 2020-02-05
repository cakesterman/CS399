import csv
import random


class Player(object):

    def __init__(self, sofifa_id, short_name, long_name, age, dob, height_cm, weight_kg, nationality, club,
                 overall, potential, player_positions):

        self.sofifa_id = sofifa_id
        self.short_name = short_name
        self.long_name = long_name
        self.age = age
        self.dob = dob
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.nationality = nationality
        self.club = club
        self.overall = overall
        self.potential = potential
        self.player_positions = player_positions
        self.bmi = round(((weight_kg / height_cm / height_cm) * 10000), 2)

    def get_short_name(self):

        return self.short_name

    def get_long_name(self):

        return self.long_name

    def get_age(self):

        return self.age

    def get_weight(self):

        return self.weight_kg

    def get_height(self):

        return self.height_cm

    def get_nationality(self):

        return self.nationality

    def get_club(self):

        return self.club

    def get_overall(self):

        return self.overall

    def get_potential(self):

        return self.potential

    def get_positions(self):

        return self.player_positions

    def get_bmi(self):

        return self.bmi

    def set_bmi(self, bmi):

        self.bmi = bmi


def read_in_csv_file():

    with open("players_20.csv", encoding="utf8") as csvfile:

        player_reader = csv.reader(csvfile)

        first_line = True

        for row in player_reader:

            # row[0] = sofifa_id
            # row[2] = short_name
            # row[3] = long_name
            # row[4] = age
            # row[5] = dob
            # row[6] = height_cm
            # row[7] = weight_kg
            # row[8] = nationality
            # row[9] = club
            # row[10] = overall
            # row[11] = potential
            # row[14] = player_positions

            # First line is the header line and we dont want to input that data as Player values
            if first_line:

                first_line = False
                continue

            player = Player(str(row[0]), str(row[2]), str(row[3]), int(row[4]), str(row[5]), int(row[6]), int(row[7]),
                            str(row[8]), str(row[9]), int(row[10]), int(row[11]), row[14])
            player_list.append(player)

            #print("Added player: {}".format(player.get_short_name()))

            # Checks if the team is not already in the dictionary, if not, adds it in
            if row[9] not in team_dict.keys():

                team_dict[row[9]] = [player]

            else:

                # if team is already in, adds player to that team
                team_dict[row[9]].append(player)

        # Prints team and the players in the team
        # for team in team_dict:
        #
        #     print(team)
        #
        #     for player in team_dict[team]:
        #
        #         print(player.get_short_name())
        #
        #     print()


def calculate_stats():

    # BMI = (weight/height / height) * 10000

    player_height_list = []

    for player in player_list:

        # Moved BMI to being calculated when player is created
        # bmi = (player.get_weight()/player.get_height() / player.get_height()) * 10000
        # bmi = round(bmi, 2)

        player_height_list.append(player.get_height())

        if player.get_bmi() > 25:

            print("{0} IS OVERWEIGHT".format(player.get_short_name()))

        elif player.get_bmi() < 18.5:

            print("{0} IS UNDERWEIGHT".format(player.get_short_name()))

        if player.get_age() > 32:

            print("{0} is close to retirement".format(player.get_short_name()))

    print("Average player height is:", round((sum(player_height_list) / len(player_height_list)), 2))


def compare_three_teams():

    team_1 = random.randint(0, len(english_premier_league_teams))
    team_2 = random.randint(0, len(english_premier_league_teams))

    # Checks to make sure that the team values are not the same and if so either increments or decrements
    if team_2 == team_1:

        if team_2 == len(english_premier_league_teams):

            team_2 -= 1

        else:

            team_2 += 1

    print("Comparing {0} and {1}".format(english_premier_league_teams[team_1], english_premier_league_teams[team_2]))

    # Compare Attackers and Defenders

    # http://logfact.com/football-soccer-field-player-positions-abbreviations/

    attacker_abv = ["ST", "CF", "SS", "RF", "RW", "RM", "LF", "LW", "LM"]
    defender_abv = ["CB", "SW", "RB", "LB", "LWB", "RWB"]

    attackers_team_1 = []
    defenders_team_1 = []

    attackers_team_2 = []
    defenders_team_2 = []

    for player in team_dict[english_premier_league_teams[team_1]]:

        if player.get_positions() in attacker_abv:

            attackers_team_1.append(player)

        if player.get_positions() in defender_abv:

            defenders_team_1.append(player)

    for player in team_dict[english_premier_league_teams[team_2]]:

        if player.get_positions() in attacker_abv:

            attackers_team_2.append(player)

        if player.get_positions() in defender_abv:

            defenders_team_2.append(player)

    def print_team_comp():

        print("ATTACKERS {}".format(english_premier_league_teams[team_1]))
        for player in attackers_team_1:

            print(player.get_short_name())

        print("DEFENDERS {}".format(english_premier_league_teams[team_2]))
        for player in defenders_team_2:

            print(player.get_short_name())

        print("ATTACKERS {}".format(english_premier_league_teams[team_2]))
        for player in attackers_team_2:

            print(player.get_short_name())

        print("DEFENDERS {}".format(english_premier_league_teams[team_1]))
        for player in defenders_team_1:

            print(player.get_short_name())

    def team_1_attack():

        for team_1_player in attackers_team_1:

            for team_2_player in defenders_team_2:

                print("Comparing height of {0}({1}cm)({2}) and {3}({4}cm)({5})".format(team_1_player.get_short_name(),
                                                                                       team_1_player.get_height(),
                                                                                       team_1_player.get_club(),
                                                                                       team_2_player.get_short_name(),
                                                                                       team_2_player.get_height(),
                                                                                       team_2_player.get_club()))

                if team_1_player.get_height() > team_2_player.get_height():

                    print("{0}(Attacker)({1}) is TALLER than {2}(Defender)({3})".format(team_1_player.get_short_name(),
                                                                                        team_1_player.get_club(),
                                                                                        team_2_player.get_short_name(),
                                                                                        team_2_player.get_club()))

                    if team_1_player.get_bmi() > team_2_player.get_bmi():

                        print("{0}(Attacker)({1}) would win against {2}(Defender)({3})".format(
                            team_1_player.get_short_name(),
                            team_1_player.get_club(),
                            team_2_player.get_short_name(),
                            team_2_player.get_club()))

                elif team_1_player.get_height() == team_2_player.get_height():

                    print("{0}(Attacker)({1}) is the SAME HEIGHT as {2}(Defender)({3})".format(
                                                                                        team_1_player.get_short_name(),
                                                                                        team_1_player.get_club(),
                                                                                        team_2_player.get_short_name(),
                                                                                        team_2_player.get_club()))

                else:

                    print("{0}(Attacker) is SHORTER than {1}(Defender)".format(team_1_player.get_short_name(),
                                                                               team_2_player.get_short_name()))

                print()

    def team_1_defend():

        for team_1_player in defenders_team_1:

            for team_2_player in attackers_team_2:

                print("Comparing height of {0}({1}cm)({2}) and {3}({4}cm)({5})".format(team_1_player.get_short_name(),
                                                                                       team_1_player.get_height(),
                                                                                       team_1_player.get_club(),
                                                                                       team_2_player.get_short_name(),
                                                                                       team_2_player.get_height(),
                                                                                       team_2_player.get_club()))

                if team_1_player.get_height() > team_2_player.get_height():

                    print("{0}(Defender) is TALLER than {1}(Attacker)".format(team_1_player.get_short_name(),
                                                                              team_2_player.get_short_name()))

                elif team_1_player.get_height() == team_2_player.get_height():

                    print("{0}(Defender) is the SAME HEIGHT as {1}(Defender)".format(team_1_player.get_short_name(),
                                                                                     team_2_player.get_short_name()))

                else:

                    print("{0}(Defender) is SHORTER than {1}(Defender)".format(team_1_player.get_short_name(),
                                                                               team_2_player.get_short_name()))

                    if team_2_player.get_bmi() > team_1_player.get_bmi():
                        print("{0}(Attacker)({1}) would win against {2}(Defender)({3})".format(
                            team_2_player.get_short_name(),
                            team_2_player.get_club(),
                            team_1_player.get_short_name(),
                            team_1_player.get_club()))

                print()

    # team_2_attack is redundant because of team_1_defend, still using it though
    def team_2_attack():

        for team_2_player in attackers_team_2:

            for team_1_player in defenders_team_1:

                print("Comparing height of {0}({1}cm)({2}) and {3}({4}cm)({5})".format(team_2_player.get_short_name(),
                                                                                       team_2_player.get_height(),
                                                                                       team_2_player.get_club(),
                                                                                       team_1_player.get_short_name(),
                                                                                       team_1_player.get_height(),
                                                                                       team_1_player.get_club()))

                if team_2_player.get_height() > team_1_player.get_height():

                    print("{0}(Attacker) is TALLER than {1}(Defender)".format(team_2_player.get_short_name(),
                                                                              team_1_player.get_short_name()))

                elif team_2_player.get_height() == team_1_player.get_height():

                    print("{0}(Attacker) is the SAME HEIGHT as {1}(Defender)".format(team_2_player.get_short_name(),
                                                                                     team_1_player.get_short_name()))

                else:

                    print("{0}(Attacker) is SHORTER than {1}(Defender)".format(team_2_player.get_short_name(),

                                                                               team_1_player.get_short_name()))

                print()

    # Not using this function as it would be redundant
    def team_2_defend():

        pass

    #print_team_comp()

    team_1_attack()
    print()
    print()
    team_1_defend()
    print()
    print()
    team_2_attack()
    print()


def print_english_premier_league_teams_and_players():

    for team_in_epl in english_premier_league_teams:

        print("PLAYERS IN {}".format(team_in_epl))

        if team_in_epl not in team_dict.keys():

            print("{} not in team dict".format(team_in_epl))

        else:

            for players in team_dict[team_in_epl]:

                print("{0}, age: {1}, weight: {2}kg, height: {3}cm, team: {4}, BMI: {5}, nationality: {6}".format(
                    players.get_short_name(), players.get_age(), players.get_weight(), players.get_height(),
                    players.get_club(),
                    players.get_bmi(), players.get_nationality()))

            print()


def print_players_in_team(team_name):

    print("PLAYERS IN {}".format(team_name))

    for players in team_dict[team_name]:

        print("{0}, age: {1}, weight: {2}kg, height: {3}cm, team: {4}, BMI: {5}, nationality: {6}".format(
            players.get_short_name(), players.get_age(), players.get_weight(), players.get_height(), players.get_club(),
            players.get_bmi(), players.get_nationality()))

    print()


def print_team_dict():

    for team in team_dict:

        print(team)

english_premier_league_teams = ["Arsenal", "Aston Villa", "Brighton & Hove Albion", "Burnley",
                                "Chelsea", "Crystal Palace", "Everton", "Leicester City", "Liverpool", "Manchester City",
                                "Manchester United", "Newcastle United", "Norwich City", "Sheffield United",
                                "Southampton", "Tottenham Hotspur", "Watford", "West Ham United",
                                "Wolverhampton Wanderers"]

player_list = []
team_dict = {}

read_in_csv_file()
calculate_stats()

print_english_premier_league_teams_and_players()

#compare_three_teams()