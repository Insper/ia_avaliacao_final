import pytest
import my_agent as agent

def config_1():
    map = [
        "0000",
        "0110",
        "0000",
    ]
    position = (0,0)
    goal = (2,3)
    return map, position, goal

def config_2():
    map = [
        "0000",
        "0110",
        "0000",
        "0000",
        "0000",
        "0000",
        "0000",
    ]
    position = (3,3)
    goal = (4,3)
    return map, position, goal

def config_3():
    # sem solucao
    map = [
        "010000",
        "011111",
        "000000",
        "000000",
    ]
    position = (3,3)
    goal = (0,4)
    return map, position, goal

def config_4():
    # mapao
    map = [
        "010000000000000000000000",
        "011111000000000000000000",
        "000000000000000000000000",
        "000000000000000000000000",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
        "010101010101010101010101",
    ]
    position = (9,4)
    goal = (0,4)
    return map, position, goal

def test_path_1():
    map, position, goal = config_1()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == [1, 1, 3, 3, 3] or actions == [3, 3, 3, 1, 1]

def test_cost_1():
    map, position, goal = config_1()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 5

def test_path_2():
    map, position, goal = config_2()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == [1] 

def test_cost_2():
    map, position, goal = config_2()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 1

def test_path_3():
    # testando o comportamento para uma situação onde não existe caminho
    map, position, goal = config_3()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert actions == None 

def test_cost_4():
    map, position, goal = config_4()
    actions = agent.parser_actions(agent.get_actions(map, position, goal))
    assert len(actions) == 13


