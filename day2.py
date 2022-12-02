points = {
    'X': 1,  # Rock/Lose
    'Y': 2,  # Paper/Draw
    'Z': 3,  # Scissors/Win
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3  # Scissors
}

outcome_scores = {
    0: 3,
    1: 0,
    2: 6
}


def calc_score(elf, player):
    return points[player] + outcome_scores[((points[elf] - points[player]) % 3)]


def calc_score_by_outcome(game):
    elf, outcome = game.split()
    player_score = (points[elf] + points[outcome]) % 3 + 1
    return player_score + outcome_scores[((points[elf] - player_score) % 3)]


with open("input/day2input.txt") as file:
    games = file.read().splitlines()
    score = sum(map(lambda x: calc_score(x[0], x[2]), games))
    print(score)
    score2 = sum(map(calc_score_by_outcome, games))
    print(score2)
