#Funcion que me muestra el jugador con mas influencia en vace a los valores dados
def calculate_influence_score_for_player(player):
    name, stats = player
    goals = stats["Goals: "]
    assists = stats["Assists:"]
    goals_avoided = stats["Goals Avoided: "]
    influence_score = (goals * 1.5) + (assists * 1) + (goals_avoided * 1.25)
    stats["Influence Score"] = influence_score
    return name, stats
def calculate_influence_score(player_stats):
    updated_player_stats = list(map(calculate_influence_score_for_player, player_stats))
    # Encuentra al jugador más influyente dentro de updated_player_stats
    most_influential_player = max(updated_player_stats, key=lambda x: x[1]["Influence Score"])
    return most_influential_player