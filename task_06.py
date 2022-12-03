class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    if len(players) > 2:
        raise WrongNumberOfPlayersError

    for player in players:
        if player[1] not in 'PSR':
            raise NoSuchStrategyError

    if len(players) == 1:
        return ' '.join(*players)

    elif (players[0][1] == players[1][1]
          or players[0][1] + players[1][1]
          in ('PR', 'SP', 'RS')):
        return ' '.join(players[0])

    return ' '.join(players[1])


print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
