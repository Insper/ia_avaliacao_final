import gymnasium as gym
import numpy as np
from QLearning import QLearning
from numpy import loadtxt
import gym_simplegrid

env = gym.make('SimpleGrid-8x8-v0', render_mode='rgb_array')

qlearn = QLearning(env, alpha=0.1, gamma=0.99, epsilon=0.8, epsilon_min=0.05, epsilon_dec=0.995, episodes=500)
q_table = qlearn.train('data/q-table-8-8.csv', 'results/rewards_8_8','results/rewards_8_8.csv')
#q_table = loadtxt('data/q-table-8-8.csv', delimiter=',')

#
# Execução depois de treinado
#

env = gym.make('SimpleGrid-8x8-v0', render_mode='human')

(x_goal, y_goal) = (7,4)
g_loc = env.to_s(x_goal, y_goal)
state, info = env.reset(options={'goal_loc':g_loc})
#state, infor = env.reset()
done = env.unwrapped.done

rewards = 0
actions = 0

while not done:
    action = np.argmax(q_table[state])
    state, reward, done, truncated, info = env.step(action)

    rewards = rewards + reward
    actions = actions + 1

print("\n")
print("Actions taken: {}".format(actions))
print("Rewards: {}".format(rewards))
