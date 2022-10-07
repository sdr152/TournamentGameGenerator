import time

def n_teams_validation(n_teams):
    if not isinstance(n_teams, int):
        print("Invalid input. Please, enter an integer.")
        return False
    if n_teams <= 2:
        print("Invalid input. There must be at least 2 teams.")
        return False
    return True

def name_validation(team_name):
    if len(team_name.split(' ')) > 2:
        print("Invalid name. No more than two words")
        return False
    length_names = [True if len(word) >= 2 else False for word in team_name.split(' ')]
    if not all(length_names):
        print("Invalid name. At least 2 characters per word")
        return False
    return True

def main():
    run = True
    while run:
        # Determine the number of teams, rounds and games.
        n_teams = int(input("Enter number of teams:  "))
        if not n_teams_validation(n_teams):
            continue
        n_rounds = int(input("Enter the number of rounds to be played: "))
        total_number_games_per_team = (n_teams - 1) * n_rounds
        print("Total number of games per team: ", total_number_games_per_team)
        
        # Name each team and validate their names.
        team_list = []   
        n = 1
        while n <= n_teams:
            team_name = input(f"Enter the name for Team {n}:  ")
            if not name_validation(team_name):
                continue
            team_list.append([team_name, 0])
            n += 1

        # Calculate how total wins are possible among all the teams.
        total_wins = 0
        for i in range(total_number_games_per_team, 0, -1*n_rounds):
            total_wins += i
        print(total_wins)
        
        # How many wins per team and validate their wins.
        max_wins = total_number_games_per_team
        for team_k in team_list:
            v = True
            while v:
                while True:
                    n_wins = input(f"Enter the number of wins Team {team_k[0]} had:  ")
                    if n_wins.isdigit():
                        n_wins = int(n_wins)
                        break
                    print("Invalid input. Try again.")

                if n_wins > max_wins:
                    continue
                team_k[1] = n_wins
                total_wins -= n_wins
                if n_wins == max_wins:
                    max_wins -= 1 * n_rounds
                if total_wins < max_wins:
                    max_wins = total_wins

                print(total_wins, max_wins, n_wins)
                break
        
        team_list.sort(key=lambda x: x[1], reverse=False)
        
        print("Generating the games to be played in the first round of the tournament...")
        time.sleep(2)
        for i in range(len(team_list)//2):
            t1 = (team_list)[i][0]
            t2 = (team_list)[-1*(i + 1)][0]
            print(f'{t1} vs. {t2}')
        print(team_list)
        
main()