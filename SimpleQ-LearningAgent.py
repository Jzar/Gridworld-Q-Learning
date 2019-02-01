#Implement Q-learning Algorithm 1 for solving Gridworld

#epsilon-greedy policy : at each step with a small probability epsilon[0,1] a random action is taken, and with probability 1 epsilon an action maximixing current estiamte q is taken

import random
import numpy as np
import time


env = Gridworld()
A = env.actions

random.seed(41)

alpha = 0.4
epsilon = 0.2
gamma = 0.95
n_episodes = 2250
n_moves = 0


#Initialize State and Q
Q = np.zeros([env.board_length*env.board_height,len(env.actions)])
S = range(env.board_length*env.board_height)

plot = []
for e in range(n_episodes):
    s = env.reset(e)
    done = False
    n_moves = 0
    while True:
        a = random.choice(A.keys()) if random.uniform(0,1) <= epsilon else np.argmax(Q[s])
        s_next, reward, done = env.move(a)
        Q[s][a] =  Q[s][a] + alpha * ( reward + gamma * np.max(Q[s_next]) - Q[s][a])
        s = s_next
        n_moves +=1
        if done:
            break
    print e, np.mean(Q)
    plot.append([e, np.mean(Q)])
