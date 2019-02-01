# Gridworld-Q-Learning
This notebook provides a custom implementation of Gridworld.

Written in Python 2

### Dependencies
- Numpy
- Jupyter ( optional )

### Installation

- In a directory of your choosing , git clone the repository. 
- To experiement with the models, open the jupyter notebook
- To run the test suite, navigate into the Girdworld-Q-Learning directory, and run test.py in shell, or otherwise
- Depending on which version of python is you default, you may have to use python2 in shell, as this is implemented in python2

### Usage
- Notebook as cell with implementation of a Gridworld class
- Part 1 is a single Q-Learning Agent
- Part 2 is an implemenation of a Q-Learning Agent class, with a shared Q function 
- Each part has a section that highlights the performance of the model, with time-steps vs. cumulative reward/step

### Purpose 

The purpose of this project is to provide an understanding of the underlying algorithms behind more complex RL (reinforcement learning) agents

### Model Evaluation

![Gridworld](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/Gridworld.png)

In this implementation of Gridworld, there is one path to the final goal state, with a choke point. The model must learn to pass 
through a single state in order to reach the goal. Following 2000 games, the Gridworld then changes its obstacles, forcing the 
agent to adapt to the new environment. Through utilizing a random epsilon-greedy policy, the model is able to adapt, as it will
still perform random actions not in its policy ( in this case, 20% of the time for Model 1, 50% for model 2)

Single Agent


![Single Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/model1-Performance.png)



3 Agent


![3 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/model2-performance.png)

4 Agent 



![4 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/Model2-4Agents.png)


5 Agent

![4 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/Model2-5agents.png)


As indicated by the above graphs, as the number of agents increase, so does the average performance of the agent, but with diminishing returns for each new agent

### Using the notebook/files

If you choose to explore using the provided notebook:
  - In order to see the gameboard, and the moves your agent are making, uncomment the "self.board()" lines in the Gridworld class
    - (Just a note, the model will make severl hundred thousand moves on its first 1-2 moves, so do this at your own warning)
  - Hyperparameters and Q functions are globally defined, make sure to clear the Q function / adjust hyperparameters in a new cell before setting up a new Async Model
  

I'm open to feedback on the implementation --- I am a student trying to learn, so feel free to contact me 
