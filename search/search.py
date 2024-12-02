# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# If you have any question, ask in Piazza or email me (mxchen21@cse.cuhk.edu.hk)
# DO NOT copy the answer from any website. You can refer to tutorial slides, but try it by yourself first! 


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from sys import path
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    def dfs_iterative(problem):
        stack = util.Stack()
        start = problem.getStartState()
        stack.push((start, []))  # Push a tuple (state, path)
        visited = set()
        visited.add(start)
        
        while not stack.isEmpty():
            try:
                state, path = stack.pop()
                if problem.isGoalState(state):
                    print("Goal is found", state)
                    print("Path is", path)
                    return path
                 
                for successor, action, cost in problem.getSuccessors(state):
                    if successor not in visited:
                        visited.add(successor)
                        new_path = path + [action]
                        stack.push((successor, new_path))
            except Exception as e:
                print(f"Error: {e}")
                pass
        
        print("No path found")
        return []

    def depthFirstSearch(problem):
        return dfs_iterative(problem)
     
    ## recursive approach 
    visited = set()
    def dfs_recursive(state): 
        print("State is", state) 
        if problem.isGoalState(state):
            return []
        try:
            negibours = problem.getSuccessors(state)
        except:
            negibours = []
        for successor, action, cost in negibours:
            if successor not in visited:
                visited.add(successor)
                new_path = dfs_recursive(successor)
                if new_path is not None:
                    return [action] + new_path
    result = dfs_recursive(problem.getStartState())
    return result

def breadthFirstSearch(problem):
    """Question 2: Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    start = problem.getStartState()
    queue.push((start, []))  # Push a tuple (state, path)
    new_path =  []
    visited = set()
    while not queue.isEmpty(): 
        state, path = queue.pop()
        print("State is", state)
        if problem.isGoalState(state):
            return path
        try:
            neighbours = problem.getSuccessors(state)
        except:
            neighbours = []
        for successor, action, cost in neighbours:
            if successor not in visited:
                visited.add(successor)
                new_path = path + [action]
                queue.push((successor, new_path))
    return new_path 

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    def UCS(state):
        # Priority queue to store nodes with their cumulative costs
        cost_map = util.Counter()
        Q = util.PriorityQueue()
        Q.push((start,[]),0)  # [(state,path), cost]
        visited = set()

        while not Q.isEmpty():
            # Pop the node with the lowest cost
            # state, total_cost, path = Q.pop()
            vertex,path = Q.pop()
            # If the state has already been visited, skip it
            if vertex in visited:
                continue

            # Mark the state as visited
            visited.add(vertex)

            # Check if we reached the goal state
            if problem.isGoalState(vertex):
                return path  # Return the path to the goal

            # Expand the node and get successors
            try:
                successors = problem.getSuccessors(vertex)
            except:
                successors = []

            for successor, action, cost in successors:
                new_cost = cost_map[vertex] + cost
                new_path = path + [action]
                
                # Push the successor into the priority queue with its new cost
                Q.push((successor, new_path),new_cost)

        return []  # Return an empty list if no path is found
    
    start = problem.getStartState()
    actions = UCS(start)
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 4: Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
