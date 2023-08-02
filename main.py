import numpy as np
import matplotlib.pyplot as plt
from environmnet import Env
from tqdm import tqdm

L_BOT = -2
L_TOP = 15
R_BOT = -3
R_TOP = 16


def run(time=10000, alpha=0.1):
    env = Env(l_bot=L_BOT, l_top=L_TOP, r_bot=R_BOT, r_top=R_TOP)
    values = np.zeros((env.l_top - env.l_bot, 2))
    for _ in tqdm(range(time)):
        l_idx, r_idx, l_floor, r_floor = env.get_floor_uniform()
        action = np.random.binomial(1, 0.5)
        if action == 0:
            reward = abs(r_floor) - abs(l_floor)
        else:
            reward = abs(l_floor) - abs(r_floor)
        delta = reward - values[l_idx][action]
        values[l_idx][action] += alpha * delta
    return values


if __name__ == "__main__":
    values = run(time=10000000, alpha=0.05)
    values = values.T
    floor_names = []
    for i in range(L_BOT, 0):
        floor_names.append(f"B{abs(i)}")
    for i in range(0, L_TOP):
        floor_names.append(f"{i+1}")
    action_names = ["stay", "right"]

    fig, ax = plt.subplots(figsize=(12, 3))

    im = ax.imshow(values)

    ax.set_yticks(np.arange(len(action_names)), labels=action_names, size=13)
    ax.set_xticks(np.arange(len(floor_names)), labels=floor_names, size=13)

    for i in range(len(action_names)):
        for j in range(len(floor_names)):
            text = ax.text(j, i, f"{values[i, j]:.1f}",
                           ha="center", va="center",
                           color="w", size=12)
    fig.colorbar(im, orientation='horizontal')
    plt.savefig("result.png")
