class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

def most_goals(team):
    return (max(team, key=lambda player: player.goals)).name # return str player name

def most_points(team):
    player=(max(team, key=lambda player: player.goals + player.passes))
    return player.name,player.number # return tuple (name,number)

def least_minutes(team):
    return min(team, key=lambda player: player.minutes) # return all player record

########################################
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))

#############################
#### proffesor solution
####
##############################

# def most_goals(ballplayers: list):
#     return max(ballplayers, key=lambda p: p.goals).name
 
# def most_points(ballplayers: list):
#     best = max(ballplayers, key=lambda p: p.goals + p.passes)
#     return (best.name, best.number)
 
# def least_minutes(ballplayers: list):
#     return min(ballplayers, key=lambda p: p.minutes)
 