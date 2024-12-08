import networkx as nx
import numpy as np


class A_star:

    def __init__(self, graph, start, goal):
        """
        Classe que implementa o algoritmo A* para busca de caminho
        :param graph: Grafo
        :param start: nó inicial
        :param goal: nó objetivo
        """
        self.graph = graph
        self.start = start
        self.goal = goal
        self.pai = {self.start: (0, 0)}
        self.path = []

    def search(self):
        """
        Algoritmo A*
        :return:
        """
        visited = set() # Conjunto de nós visitados
        queue = [(self.start, 0)]  # A fila armazena os nós junto com o custo acumulado

        # Enquanto a fila não estiver vazia
        while queue:
            # Ordena a fila com base no custo (g + h)
            queue = sorted(queue, key=lambda x: x[1] + self.graph.G.nodes[x[0]]['heuristic'])
            node, cost = queue.pop(0)  # Pega o nó com o menor custo

            # Se o nó não foi visitado, evita que um nó seja visitado mais de uma vez
            if node not in visited:
                visited.add(node) # Adiciona o nó ao conjunto de visitados
                self.path.append(node) # Adiciona o nó ao caminho

                # Se o nó for o objetivo, termina a busca
                if node == self.goal:
                    break

                # Verifica os vizinhos
                for neighbor in self.graph.G.neighbors(node):
                    # Se o vizinho não foi visitado
                    if neighbor not in visited:
                        # Novo custo para o vizinho, soma do custo acumulado com o custo da aresta
                        new_cost = cost + self.graph.G[node][neighbor]['weight']

                        # Se for a primeira vez que encontramos o vizinho ou se o caminho é melhor (evita que o um nó na fila não seja atualizado)
                        if neighbor not in self.pai or new_cost < self.pai[neighbor][1]:
                            self.pai[neighbor] = (node, new_cost)  # Armazena o pai e o custo

                        # Adiciona o vizinho a fila
                        queue.append((neighbor, new_cost)) # Pode adicionar um nó mais de uma vez, mas com custos diferentes, o menor custo é escolhido


    def best_path(self):
        """
        Extrai o melhor caminho
        :return: melhor caminho
        """
        path_best = [] # Caminho final
        no_atual = self.goal # Nó atual é o objetivo

        # Reconstrua o caminho a partir do objetivo, seguindo os pais
        while no_atual != self.start:
            path_best.append(no_atual) # Adiciona o nó atual ao caminho
            no_atual = self.pai[no_atual][0]  # Pega o pai do nó atual

        path_best.append(self.start) # Adiciona o nó inicial ao caminho
        path_best.reverse() # Inverte o caminho

        return path_best

