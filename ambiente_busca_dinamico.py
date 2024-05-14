import gymnasium as gym
import gym_simplegrid
import my_agent as agent

env = gym.make('SimpleGrid-8x8-v0', render_mode='human')
map = gym_simplegrid.envs.simple_grid.MAPS['8x8']

obs, info = env.reset()

position = info['agent_xy']
(x_goal, y_goal) = env.goal_xy
done = env.unwrapped.done
reward_total = 0
   
actions = agent.parser_actions(agent.get_actions(map, position, (x_goal, y_goal)))

if actions != None:

    count_actions = 0
    while not done and count_actions < 1000:
        # remove o primeiro elemento da lista de ações
        action = actions.pop(0)
        obs, reward, done, _, info = env.step(action)
        reward_total += reward
        count_actions += 1
    env.close()

    print(f"Total de recompensa: {reward_total}")
    print(f"Total de ações: {count_actions}")

else:
    print("Não existe solução")
    env.close()