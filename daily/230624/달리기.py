def solution(players, callings):
    n = len(players)
    
    ranking = []
    idxset = {}
    for i in range(n):
        ranking.append(players[i])
        idxset[players[i]] = i
    
    for j in callings:
        a = idxset[j]
        rank = ranking[a - 1]
        
        ranking[a - 1] = j
        ranking[a] = rank
        
        idxset[j] = a - 1
        idxset[rank] = a
        
    return ranking