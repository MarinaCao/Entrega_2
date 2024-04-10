#Calculo promedio de goles de los 25 partidos
def calculate_team_average_goals(player_stats, total_matches):
    total_goals = sum(stats["Goals: "] for _, stats in player_stats)
    average_goals = total_goals / total_matches
    return average_goals