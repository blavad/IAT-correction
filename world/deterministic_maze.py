import os
import world.maze_generator
from world.maze_generator import MazeGenerator

class DeterministicMazeModel:
    URL_DET_MAZE = os.path.join(os.path.dirname(world.maze_generator.__file__), "det_maze.txt")

    actions = ['up','down','left','right']

    def __init__(self):
        pass 
    
    def T(self, state, action, next_state):
        action_name = self.actions[action]
        proba = 0.
        if action_name == 'up':    # up
            if (self.maze[state[0]-1, state[1]] == 0) and (next_state == (state[0]-1, state[1])): # can go up
                proba = 1  
            elif (self.maze[state[0]-1, state[1]] == 1) and (next_state == state): # cant go up
                proba = 1
        elif action_name == 'down':  # down
            if (self.maze[state[0]+1, state[1]] == 0) and (next_state == (state[0]+1, state[1])): # can go down
                proba = 1  
            elif (self.maze[state[0]+1, state[1]] == 1) and (next_state == state): # cant go down
                proba = 1
        elif action_name == 'left':  # left
            if (self.maze[state[0], state[1]-1] == 0) and (next_state == (state[0], state[1]-1)): # can go left
                proba = 1  
            elif (self.maze[state[0], state[1]-1] == 1) and (next_state == state): # cant go left
                proba = 1
        else:              # right
            if (self.maze[state[0], state[1]+1] == 0) and (next_state == (state[0], state[1]+1)): # can go right
                proba = 1  
            elif (self.maze[state[0], state[1]+1] == 1) and (next_state == state): # cant go right
                proba = 1

        return proba

    def R(self, state, action):
        return -1