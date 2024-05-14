import numpy as np
import random
from numpy import savetxt
import sys
import matplotlib.pyplot as plt
import pandas as pd

class QLearning:

    def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
        self.env = env
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes

    def select_action(self, state):
        rv = random.uniform(0, 1)
        if rv < self.epsilon:
            return self.env.action_space.sample() # Explore action space
        return np.argmax(self.q_table[state]) # Exploit learned values

    def train(self, filename, plotFile, rewardsCsvFile):

        df = pd.DataFrame(columns=['Episode', 'Epsilon', 'Actions', 'Rewards'])

        for i in range(1, self.episodes+1):

            (x_goal, y_goal) = (7,4)
            g_loc = self.env.to_s(x_goal, y_goal)
            (state, _) = self.env.reset(options={'goal_loc':g_loc})
            #(state, _) = self.env.reset()
            (x_inicio, y_inicio) = self.env.to_xy(state)

            rewards = 0
            done = False
            actions = 0

            while not done and actions < 200:
                action = self.select_action(state)
                next_state, reward, done, truncated, _ = self.env.step(action) 
        
                old_value = self.q_table[state, action] #pegar o valor na q-table para a combinacao action e state
                next_max = np.max(self.q_table[next_state]) #np.max(`do maior valor considerando next_state`)
                new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)  #calcula o novo valor
                self.q_table[state, action] = new_value
                
                state = next_state
                actions=actions+1
                rewards=rewards+reward

            (x_goal, y_goal) = self.env.to_xy(state)
            print(f'Goal: {(x_goal, y_goal)} Local início: {(x_inicio, y_inicio)} Episodes: {str(i)} Epsilon: {str(self.epsilon)} Ações: {str(actions)} Recompensas: {str(rewards)}')
            new_record = pd.DataFrame({'Episode': [i], 'Epsilon': [self.epsilon], 'Actions': [actions], 'Rewards': [rewards]})
            df = pd.concat([df,new_record], ignore_index=True)

            if self.epsilon > self.epsilon_min:
                self.epsilon = self.epsilon * self.epsilon_dec

        savetxt(filename, self.q_table, delimiter=',')
        df.to_csv('./data/dados_treinamento.csv', index=False)

        return self.q_table

    def save_rewards(self, rewards_per_episode, filename):
        np.savetxt(filename, rewards_per_episode, delimiter=",")
