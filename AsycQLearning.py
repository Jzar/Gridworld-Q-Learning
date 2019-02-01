from threading import Thread
from threading import Semaphore
## defining our agent as a class that can be threaded



from Gridworld import Gridworld



import random
import numpy as np
import time
"""
Example Hyperparameter set up

#Environment and hyperparameters
env = Gridworld()
A = env.actions
random.seed(41)
alpha = .2
epsilon = .5
gamma = 0.95
n_episodes = 2250
n_moves = 0
AsyncUpdate = 5


#Initialize State and Q
Q = np.zeros([env.board_length*env.board_height,len(env.actions)])
S = range(env.board_length*env.board_height)
T = 0

How to use the class:

start calls run concurrently with other agents,
join brings the agent back to the main thread one its finished run

agent = agent(alpha,epsilon,gamma,n_episodes,S,A,env)
agent.start()
agent.join()
"""

#make writing to global Q thread safe with Semaphore
writingQ = Semaphore(1)

class agent(Thread):
    def __init__(self,alpha, epsilon,gamma, n_episodes,S,A,env):
        Thread.__init__(self)
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.n_episodes=n_episodes
        self.delta_Q = np.zeros([env.board_length*env.board_height,len(env.actions)])
        self.S = S
        self.A = A
        self.plot = []
        self.env = env

    def run(self):
        for e in range(self.n_episodes):
            s = self.env.reset(e)
            done = False
            n_moves = 0
            while True:
                a = random.choice(self.A.keys()) if random.uniform(0,1) <= self.epsilon else np.argmax(Q[s])
                s_next, reward, done = self.env.move(a)
                self.delta_Q[s][a] =self.delta_Q[s][a] + self.alpha * ( reward + self.gamma * np.max(Q[s_next]) - Q[s][a])
                s = s_next
                
                if n_moves % AsyncUpdate == 0:
                    self.update()
                if done:
                    self.update()
                    break
                n_moves +=1
                #T += 1
            self.plot.append([e, np.mean(Q)])
    def update(self):
        writingQ.acquire()
        for i in range(54):
            for j in range(4):
                Q[i][j] = Q[i][j] + self.alpha * self.delta_Q[i][j]
        self.delta_Q = np.zeros([self.env.board_length*self.env.board_height,len(self.env.actions)])
 
        writingQ.release()
