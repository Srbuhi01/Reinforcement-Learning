import numpy as np
from tqdm import tqdm

from src.models import TrivialModel, TimeModel

def choose_action(state, action_value_estimates, maze, dyna_params):
    # region Summary
    """
    Choose an action based on 𝜀-greedy algorithm
    :param state: State
    :param action_value_estimates: Action-value estimates (denoted as 𝑄(𝑆_𝑡, 𝐴_𝑡))
    :param maze: Maze instance containing all information about the environment
    :param dyna_params: Parameters of Dyna algorithms
    :return: Action
    """
    # endregion Summary

    # region Body

    # ε-greedy action selection: every once in a while, with small probability ε, select randomly from among all the actions with equal probability, independently of the action-value estimates.
    if np.random.binomial(n=1, p=dyna_params.exploration_probability) == 1:
        action = np.random.choice(list(maze.actions.values()))

    # Greedy action selection: select one of the actions with the highest estimated value, that is, one of the greedy actions.
    # If there is more than one greedy action, then a selection is made among them in some arbitrary way, perhaps randomly.
    else:
        values = action_value_estimates[state[0], state[1], :]
        action = np.random.choice([act for act, val in enumerate(values) if val == np.max(values)])

    return action

    # endregion Body

# region Dyna Maze

def dyna_q(action_value_estimates, model, maze, dyna_params):
    # region Summary
    """
    Play for an episode for Dyna-Q algorithm
    :param action_value_estimates: Action-value estimates (denoted as 𝑄(𝑆_𝑡, 𝐴_𝑡))
    :param model: Model instance for planning
    :param maze: Maze instance containing all information about the environment
    :param dyna_params: Parameters of Dyna algorithms
    :return: Steps
    """
    # endregion Summary

    # region Body

    # Start at the maze's start state


    # Initialize a counter for steps to 0


    # While the agent hasn't reached its goal

        # track the steps


        # choose an action


        # get the next state and reward


        # perform Q-Learning update


        # feed the model with experience


        # sample experience from the model


        # move to next state


        # check whether it has exceeded the step limit




    # endregion Body

# endregion Dyna Maze

# region Changing Maze

def changing_maze(maze, dyna_params):
    # region Summary
    """
    Wrapper function for changing maze.
    :param maze: Maze instance containing all information about the environment
    :param dyna_params: Parameters of Dyna algorithms
    :return: Rewards
    """
    # endregion Summary

    # region Body

    # Set up max steps


    # Track the cumulative rewards


    # For every run

        # set up models


        # initialize state-action value estimates with 0s


        # for every method

            # print('run:', run, dyna_params.methods[i])

            # set old obstacles for the maze


            # initialize a counter for steps to 0


            # get the last steps


            # while the max steps hasn't been reached

                # play for an episode


                # update cumulative rewards


                # get the last steps


                # if it's time to change the obstacles

                    # change the obstacles


    # Average rewards




    # endregion Body

# endregion Changing Maze

# region Prioritized Sweeping

def prioritized_sweeping(action_value_estimates, model, maze, dyna_params):
    # region Summary
    """
    Play for an episode for prioritized sweeping algorithm
    :param action_value_estimates: Action-value estimates (denoted as 𝑄(𝑆_𝑡, 𝐴_𝑡))
    :param model: Model instance for planning
    :param maze: Maze instance containing all information about the environment
    :param dyna_params: Parameters of Dyna algorithms
    :return: Number of backups during this episode
    """
    # endregion Summary

    # region Body

    # Start at the maze's start state


    # Track the number of steps in this episode


    # Track the number of backups in planning phase


    # While the agent hasn't reached its goal

        # increment the number of steps


        # choose an action


        # get the next state and reward


        # feed the model with experience


        # get the priority for current state-action pair


        # check whether priority exceeds threshold


        # start planning


        # planning for several steps (although, keep planning until the priority queue becomes empty will converge much faster)

            # get a sample with the highest priority from the model


            # update the state action value for the sample


            # update action-value estimates


            # deal with all the predecessors of the sample state


                # check whether priority exceeds threshold


            # increment the planning step


        # move to the next state


        # update the number of backups


    return backups

    # endregion Body

def check_path(action_value_estimates, maze):
    # region Summary
    """
    Check whether state-action values are already optimal
    :param action_value_estimates: Action-value estimates (denoted as 𝑄(𝑆_𝑡, 𝐴_𝑡))
    :param maze: Maze instance containing all information about the environment
    :return: True, if state-action values are already optimal; otherwise, False
    """
    # endregion Summary

    # region Body

    # Set the length of optimal path of the original maze
    original_length = 14

    # Relaxed optimal path
    relaxed_optimal_path = 1.2

    # Get the length of optimal path
    max_steps = original_length * maze.resolution * relaxed_optimal_path

    # Start at the maze's start state
    state = maze.start

    # Track the number of steps in this episode
    steps = 0

    # While the agent hasn't reached its goal
    while state not in maze.goals:
        # get the action with maximum estimated value
        action = np.argmax(action_value_estimates[state[0], state[1], :])

        # get the state
        state, _ = maze.step(state, action)

        # increment the number of steps
        steps += 1

        # check whether the number of steps exceeds maximum
        if steps > max_steps:
            return False

    return True

    # endregion Body

# endregion Prioritized Sweeping