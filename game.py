# Version 2

import time

def number_teams():
    while True:
        n_teams = input("Enter the number of teams:  ")
        
        if not n_teams.isdigit():
            print("Invalid input. Please, enter an integer.")
            continue
        if int(n_teams) < 2:
            print("Invalid input. There must be at least 2 teams in the tournament.")
            continue
        if int(n_teams) % 2 != 0:
            print("Invalid input. There must be an even number of teams.")
            continue
        return int(n_teams)

def tournament_info(n_teams):
    while True:
        n_rounds = input("Enter the number of rounds:  ")
        
        if not n_rounds.isdigit():
            print("Invalid input. Please, enter a digit.")
            continue
        if int(n_rounds) < 1:
            print("Invalid input. There must be at least 1 round in the tournament.")
            continue
        num_games_per_team = (n_teams - 1) * int(n_rounds)
        print(f'Number of games per team: {num_games_per_team}')
        print(f'Number of rounds to play: {n_rounds}')

        # Calculate the max number of win in the tournament among all teams
        # Apply n(n+1) / 2 if only 1 round.
        total_possible_wins = 0
        for i in range(num_games_per_team, 0, -1*int(n_rounds)):
            total_possible_wins += i
        print(total_possible_wins)
        return num_games_per_team, int(n_rounds), total_possible_wins

def generate_teams(n_teams):
    teams_list = []
    n = 1
    while n <= n_teams:
        team_name = input(f"Enter the name for Team {n}:  ")
        if not name_validation(team_name):
            continue
        teams_list.append(team_name)
        n += 1
    return teams_list

def name_validation(team_name):
    if len(team_name.split(' ')) > 2:
        print("Invalid name. No more than two words")
        return False
    length_names = [True if len(word) >= 2 else False for word in team_name.split(' ')]
    if not all(length_names):
        print("Invalid name. At least 2 characters per word")
        return False
    return True

def get_team_wins(teams_list, number_games_per_team, total_possible_wins, n_rounds):
    team_wins = []
    max_wins = number_games_per_team

    for tm in teams_list:
        run = True
        while run:
            n_wins = input(f"Enter the number of wins Team {tm} had:  ")
            if not n_wins.isdigit():
                print('1. Invalid input. Please, enter a positive integer.')
                continue
            n_wins = int(n_wins)
            if n_wins > max_wins:
                print(f'Invalid input. Only {max_wins} number of wins available.')
                continue
            team_wins.append((tm, n_wins))
            total_possible_wins -= n_wins
            if n_wins == max_wins:
                max_wins -= 1 * n_rounds
            if total_possible_wins < max_wins:
                max_wins = total_possible_wins

            print(total_possible_wins, max_wins, n_wins)
            break
        return team_wins

def main():
    run = True
    while run:
        # Determine the number of teams, rounds and games.
        n_teams = number_teams()
        number_games_per_team, n_rounds, total_possible_wins = tournament_info(n_teams)
        
        # Name each team and validate their names.
        teams_list = generate_teams(n_teams)

        # How many wins per team and validate their wins.
        team_wins = get_team_wins(teams_list, number_games_per_team, total_possible_wins, n_rounds)
        team_wins.sort(key=lambda x: x[1], reverse=False)
        
        print("Generating the games to be played in the first round of the tournament...\n")
        time.sleep(2)
        for i in range(len(teams_list)//2):
            t1 = (team_wins)[i][0]
            t2 = (team_wins)[-1*(i + 1)][0]
            print(f'{t1} vs. {t2}')
        print(team_wins)   
main()