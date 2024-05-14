import gymnasium as gym
import gym_simplegrid

env = gym.make('SimpleGrid-8x8-v0', render_mode='human')
obs, info = env.reset()
done = env.unwrapped.done

count_actions = 0
while not done and count_actions < 100:
    action = env.action_space.sample()
    obs, reward, done, _, info = env.step(action)
    count_actions += 1
    
env.close()