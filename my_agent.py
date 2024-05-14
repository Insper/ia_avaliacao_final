from aigyminsper.search.Graph import State

class MyAgent(State):

    #
    # TODO implemente o seu agente
    #

    def successors(self):
        #
        # TODO Os sucessores que devem ser considerados são: 
        # 0 - cima
        # 1 - baixo
        # 2 - esquerda
        # 3 - direita
        #
        # IMPORTANTE: para todo estado sempre deve-se retornar 4 sucessores
        #
        sucessors = []
        return sucessors

    def description(self):
        return "Agente que sabe andar em um grid simples"


def get_actions(map, position, goal):
    #
    # TODO Esta função deve retornar uma lista de ações que o agente deve executar
    # Assim conseguimos executar o agente no ambiente usando a biblioteca
    # gym_simplegrid
    #
    # Se nao existir solucao, a funcao deve retornar None
    #
    return None

def parser_actions(str_actions):
    if str_actions != None:
        actions = str_actions.split(';')
        actions = list(map(int, actions[1:]))
        return actions
    return None

