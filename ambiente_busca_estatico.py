import gymnasium as gym
import gym_simplegrid
import my_agent as agent

obstacle_map = [
        "10000000",
        "10011000",
        "00001001",
        "01001001",
        "01001001",
        "01001001",
        "01001001",
    ]

env = gym.make(
    'SimpleGrid-v0', 
    obstacle_map=obstacle_map, 
    render_mode='human'
)

position = (0,5)
(x_goal, y_goal) = (6,2)
s_loc = position[0] * len(obstacle_map[0]) + position[1]
g_loc = x_goal * len(obstacle_map[0]) + y_goal

obs, info = env.reset(options={'start_loc':s_loc, 'goal_loc':g_loc})

position = info['agent_xy']
(x_goal, y_goal) = env.goal_xy
done = env.unwrapped.done
reward_total = 0
   
actions = agent.parser_actions(agent.get_actions(obstacle_map, position, (x_goal, y_goal)))

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