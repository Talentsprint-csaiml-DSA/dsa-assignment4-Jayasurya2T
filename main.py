def stable_marriage(n, boy_preferences, girl_preferences):
    # Array to keep track of which girl is currently paired with which boy
    girl_partner = [-1] * n  # Initially no girl is paired
    boy_free = [True] * n    # All boys are initially free
    proposals_count = [0] * n  # Number of proposals each boy has made
    
    # Create a preference ranking dictionary for girls
    girl_rankings = [{} for _ in range(n)]
    for i in range(n):
        for rank, boy in enumerate(girl_preferences[i]):
            girl_rankings[i][boy] = rank
    
    free_count = n  # Number of free boys

    while free_count > 0:
        # Find the first free boy
        boy = -1
        for i in range(n):
            if boy_free[i]:
                boy = i
                break
        
        # Find the girl he is proposing to
        girl = boy_preferences[boy][proposals_count[boy]] - 1
        proposals_count[boy] += 1

        if girl_partner[girl] == -1:
            # If the girl is free, they become engaged
            girl_partner[girl] = boy
            boy_free[boy] = False
            free_count -= 1
        else:
            # If the girl is already engaged, check if she prefers the new boy
            current_partner = girl_partner[girl]
            if girl_rankings[girl][boy + 1] < girl_rankings[girl][current_partner + 1]:
                # She prefers the new boy
                girl_partner[girl] = boy
                boy_free[boy] = False
                boy_free[current_partner] = True

    # Output the final matches
    matches = []
    for girl in range(n):
        matches.append((girl_partner[girl] + 1, girl + 1))  # +1 to match the 1-based indexing
    return matches
