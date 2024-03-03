def rand_bool(prob):
    return random.random() < prob

def stupid_game(n, data):
    goals = 0
    for i in range(n):
        goals += rand_bool(data[random.randint(0,3)])
    return goals

def smart_taker(n, data):
    goals = 0
    for i in range(n):
        goals += rand_bool(data[2 + random.randint(0,1)])
    return goals

def smart_keeper(n, data):
    goals = 0
    for i in range(n):
        goals += rand_bool(data[random.choice([1,3])])
    return goals

def nash_eq(n, data):
    goals = 0
    for i in range(n):
        curr = random.random()
        if curr <= 0.251:
            goals += rand_bool(data[0])
        elif curr <= 0.44:
            goals += rand_bool(data[1])
        elif curr <= 0.759:
            goals += rand_bool(data[2])
        else: goals+= rand_bool(data[3])
    return goals

