import numpy as np


class Gridworld:
    
    def __init__(self):
        #"LEFT,RIGHT,UP,DOWN"
        self.actions = {0: (-1,0),1:(1,0),2:(0,1),3:(0,-1)}


        self.board_length= 9
        self.board_height= 6

        self.obstacles = [i+2*self.board_length for i in range(8)]
        self.done = False
        self.goal = 8 + self.board_length * 5
        self.start = 3 + self.board_length * 0
        self.score = 0
        self.player = self.start

    def move(self,action):
        state = self.player
        new_state = (state + (self.actions[action][0] + self.board_length*self.actions[action][1]))
        #if new state is valid
        if(new_state not in self.obstacles and self.board_length * self.board_height > new_state > 0 ):
            if(new_state ==self.goal):
                self.done = True
                self.score = 1
               # print "Winner!"
        else:
            new_state = state
            self.score = 0
            #print "You can't do that"
        self.player = new_state
        self.board()
        return (new_state,self.score,self.done)
    def reset(self,e):
        
        self.done = False
        self.score = 0
        self.player = self.start
        self.obstacles = self.obstacles if e < 2000 else [i+2*self.board_length for i in range(1,9)]
        #print self.player,self.goal
        #self.board()
        return self.player
        
    def board(self):
        state = self.player
        
        #go through every row, then every element in that row
        #Format it into a string, and print to console
        s = ""
        board = []
        for i in range(self.board_length*self.board_height):
            #print(i,j)
            if (i % 9 == 0 ):
                
                board.append(s)
                s = ""
            if i in self.obstacles:
                s+= "[X]\t"
            elif i == self.player:
                s+="[A]\t"
                print
            elif i == self.goal:
                s+="[G]\t"
            elif i == self.start:
                s+="[S]\t"
            else:
                s+="[ ]\t"
        board.append(s)
        for i in board[::-1]: print i
        print('\n')
