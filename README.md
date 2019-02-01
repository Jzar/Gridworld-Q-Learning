# Gridworld-Q-Learning
This notebook provides a custom implementation of Gridworld.


### Dependencies
- Numpy

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



![Single Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/model1-Performance.png)


![3 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/model2-performance.png)

![4 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/Model2-4agents.png)

![4 Agent Q-Learning](https://raw.githubusercontent.com/Jzar/Gridworld-Q-Learning/master/model2-5agents.png)


As indicated by the above graphs, as the number of agents increase, so does the average performance of the agent.
