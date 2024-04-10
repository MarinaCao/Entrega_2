#Funcion de buscar el goleador/a con mas goles echos
def sub_inciso2(player_stats):
    top_scorer = max(player_stats, key=lambda x: x[1]['Goals: '])
    return top_scorer