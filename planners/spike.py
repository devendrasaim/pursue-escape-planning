import numpy as np
from typing import List, Tuple, Optional
import heapq
import math
import random


class Node:
    def __init__(self, state, parent=None):
        self.state = state            # (grid, current_pos, pursued_pos, pursuer_pos)
        self.parent = parent
        self.children: List[Node] = []
        self.visits = 0
        self.value = 0.0
        self.action = None            # action taken from parent to reach this node

    def get_actions(self) -> List[Tuple[int,int]]:
        return [(0,0),(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

    def is_fully_expanded(self) -> bool:
        return len(self.children) == len(self.get_actions())

    def expand(self) -> 'Node':
        tried = {child.action for child in self.children}
        for a in self.get_actions():
            if a not in tried:
                next_state = self.sim(self.state, a)
                child = Node(next_state, parent=self)
                child.action = a
                self.children.append(child)
                return child
        raise RuntimeError("No actions left to expand")

    def best_child(self, c_param=1.4) -> 'Node':
        choices = []
        for child in self.children:
            if child.visits == 0:
                uct = float('inf')
            else:
                uct = (child.value/child.visits) + c_param * math.sqrt(2*math.log(self.visits)/child.visits)
            choices.append(uct)
        return self.children[int(np.argmax(choices))]

    def rollout_policy(self, actions):
        grid, cur, pursued, pursuer = self.state
        scores = []
        for a in actions:
            next_pos = (cur[0] + a[0], cur[1] + a[1])
            # Reward moving towards target
            target_dist = math.sqrt((next_pos[0] - pursued[0])**2 + (next_pos[1] - pursued[1])**2)
            # Penalize moving towards pursuer
            pursuer_dist = math.sqrt((next_pos[0] - pursuer[0])**2 + (next_pos[1] - pursuer[1])**2)
            score = -target_dist + pursuer_dist
            scores.append(score)
        
        # Convert scores to probabilities
        scores = np.array(scores)
        probs = np.exp(scores - np.max(scores))
        probs = probs / probs.sum()
        return actions[np.random.choice(len(actions), p=probs)]

    def sim(self, state, action):
        grid, cur, pursued, pursuer = state
        rows, cols = grid.shape
        
        # Spike's next position
        nxt_cur = (cur[0]+action[0], cur[1]+action[1])
        
        # Tom (pursued) moves towards Jerry
        nxt_pursued = self.move(grid, pursued, cur)
        
        # Jerry (pursuer) moves towards Spike
        nxt_pursuer = self.move(grid, pursuer, cur)
        
        return (grid, nxt_cur, nxt_pursued, nxt_pursuer)

    def move(self, grid, pos, target):
        rows, cols = grid.shape
        best_move = None
        best_dist = float('inf')
        
        for a in self.get_actions():
            np_ = (pos[0]+a[0], pos[1]+a[1])
            if 0 <= np_[0] < rows and 0 <= np_[1] < cols and grid[np_]==0:
                dist = math.sqrt((np_[0] - target[0])**2 + (np_[1] - target[1])**2)
                if dist < best_dist:
                    best_dist = dist
                    best_move = np_
        
        return best_move if best_move is not None else pos

    def rollout(self) -> float:
        state = self.state
        grid, cur, pursued, pursuer = state
        depth = 20  # Increased depth for better simulation
        grid_size = grid.shape[0]
        
        for _ in range(depth):
            # Terminal checks
            if cur[0] < 0 or cur[0] >= grid_size or cur[1] < 0 or cur[1] >= grid_size:
                return -1.0  # Out of bounds
            
            if cur == pursued and grid[cur]==0:
                return 1.0  # Captured target
            
            if cur == pursuer or grid[cur]==1:
                return -1.0  # Caught or crashed
            
            # Calculate distances for reward
            target_dist = math.sqrt((cur[0] - pursued[0])**2 + (cur[1] - pursued[1])**2)
            pursuer_dist = math.sqrt((cur[0] - pursuer[0])**2 + (cur[1] - pursuer[1])**2)
            
            # Intermediate reward based on distances
            if target_dist < 2:  # Very close to target
                return 0.8
            if pursuer_dist < 2:  # Very close to pursuer
                return -0.8
            
            # Biased random step
            a = self.rollout_policy(self.get_actions())
            state = self.sim(state, a)
            grid, cur, pursued, pursuer = state
            
        # Default: no decisive outcome
        return 0.0

    def bp(self, reward):
        self.visits += 1
        self.value += reward
        if self.parent:
            self.parent.bp(reward)


class MCTS:
    """Monte Carlo Tree Search."""
    def __init__(self, iterations=200):  # Increased iterations
        self.iterations = iterations

    def search(self, init_state):
        root = Node(init_state)
        for _ in range(self.iterations):
            node = root
            # 1. Selection
            while node.children and node.is_fully_expanded():
                node = node.best_child()
            # 2. Expansion
            if node.visits > 0 and not node.is_fully_expanded():
                node = node.expand()
            # 3. Simulation
            reward = node.rollout()
            # 4. Backpropagation
            node.bp(reward)
        # Choose the child with highest visit count
        best = root.best_child(c_param=0.0)
        return best.action


class PlannerAgent:
    def __init__(self):
        pass
    
    def plan_action(self, world: np.ndarray, current: np.ndarray, pursued: np.ndarray, pursuer: np.ndarray) -> Optional[np.ndarray]:
        """
        Computes an action to take from the current position to capture the pursued while evading from the pursuer.

        Parameters:
        - world (np.ndarray): A 2D numpy array representing the grid environment.
        - 0 represents a walkable cell.
        - 1 represents an obstacle.
        - current (np.ndarray): The (row, column) coordinates of the current position.
        - pursued (np.ndarray): The (row, column) coordinates of the agent to be pursued.
        - pursuer (np.ndarray): The (row, column) coordinates of the agent to evade from.

        Returns:
        - np.ndarray: one of the 9 actions from 
                              [0,0], [-1, 0], [1, 0], [0, -1], [0, 1],
                                [-1, -1], [-1, 1], [1, -1], [1, 1]
        """
        # Convert positions to tuples
        current_pos = (int(current[0]), int(current[1]))
        pursued_pos = (int(pursued[0]), int(pursued[1]))
        pursuer_pos = (int(pursuer[0]), int(pursuer[1]))
        
        # Initialize MCTS and search for best action
        mcts = MCTS(iterations=200)
        init_state = (world, current_pos, pursued_pos, pursuer_pos)
        best_action = mcts.search(init_state)
        
        # Convert action to numpy array
        return np.array(best_action)


