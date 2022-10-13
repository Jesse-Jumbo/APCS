def ball_game(home_first, away_first, home_second, away_second):
    home_first_score = [int(x) for x in home_first.split()]
    away_first_score = [int(x) for x in away_first.split()]
    home_second_score = [int(x) for x in home_second.split()]
    away_second_score = [int(x) for x in away_second.split()]
    home = {"home": sum(home_first_score), "away": sum(away_first_score)}
    away = {"home": sum(home_second_score), "away": sum(away_second_score)}

    if home["home"] > home["away"] and away["home"] > away["away"]:
        res = "Win"
    elif home["home"] < home["away"] and away["home"] < away["away"]:
        res = "Lose"
    else:
        res = "Tie"

    print(f'{home["home"]}:{home["away"]}')
    print(f'{away["home"]}:{away["away"]}')
    print(res)


ball_game(input(), input(), input(), input())
