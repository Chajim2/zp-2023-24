from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import random

random.seed()

df = pd.read_excel(open('penalties.xlsx','rb'))
df = df.dropna(how='all').dropna(how='all', axis=1)

shots = [0] * 9
goals = [0] * 9
dives = {
    "R" : 0,
    "C" : 0,
    "L" : 0
}

for index, row in df.iterrows():
    try:
        if row["Keeper"] == "L":
            shots[int(row["Zone"])% 3] += 1
            goals[int(row["Zone"])% 3] += int(row["Goal"])
        elif row["Keeper"] == "C":
            shots[int(row["Zone"])% 3 + 3] += 1
            goals[int(row["Zone"])% 3 + 3] += int(row["Goal"])
        elif row["Keeper"] == "R":
            shots[int(row["Zone"])% 3 + 6] += 1
            goals[int(row["Zone"])% 3 + 6] += int(row["Goal"])
    except:
        pass

simplified_data = [
    goals[1] / shots[1],
    goals[7] / shots[7],
    goals[0] / shots[0],
    goals[6] / shots[6]
]


def print_table(goals,shots):
    data = [
        ["shot left", goals[1] / shots[1],goals[4] / shots[4],goals[7] / shots[7]],
        ["shot center", goals[2] / shots[2], goals[5] / shots[5],goals[8] / shots[8]],
        ["shot right", goals[0] / shots[0], goals[3] / shots[3],goals[6] / shots[6]],
    ]
    print(tabulate(data, headers = ["x", "dived left", "center" , "dived right"],tablefmt="fancy_grid" ))
    print(shots)

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
        if curr <= 0.4:
            goals += rand_bool(data[0])
        elif curr <= 0.69:
            goals += rand_bool(data[1])
        elif curr <= 0.87:
            goals += rand_bool(data[2])
        else: goals+= rand_bool(data[3])
    return goals



def create_graph(y_data, x_data, y_name, x_name):
    plt.bar(x_data, y_data, color = "red")
    plt.x_label = x_name
    plt.y_label = y_name
    plt.ylim(600000,800000)
    plt.show()
create_graph([nash_eq(1000000, simplified_data),smart_keeper(1000000,simplified_data),stupid_game(1000000,simplified_data),smart_taker(1000000,simplified_data)],
            ["Nashovo equilibrium", "Intel. Brankář","Náhodný výběr", "Intel. střelec"], "strategie","počet gólů z 1 000 000 střel " )

