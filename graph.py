import networkx as nx


class Graph:

    def __init__(self, matrix):
        """
        Classe para criar um grafo a partir de uma matriz
        :param matrix: Matriz do mapa
        """
        self.G = nx.Graph()
        self.matrix = matrix

    def create_graph(self):
        """
        Cria o grafo a partir da matriz
        :return:
        """

        rows, cols = self.matrix.shape  # Pega o tamanho da matriz
        for i in range(rows):  # Para cada linha
            for j in range(cols):  # Para cada coluna
                if self.matrix[i, j] != 0:  # Se o valor da matriz for diferente de 0, 0 é água/parade
                    self.G.add_node((i, j))  # Adiciona o nó ao grafo

        for i in range(rows):  # Para cada linha
            for j in range(cols):  # Para cada coluna
                if self.matrix[i, j] != 0:  # Se o valor da matriz for diferente de 0, 0 é água/parade
                    if j + 1 < cols and self.matrix[i, j + 1] != 0:  # Se a próxima coluna não for água
                        # Adiciona a aresta entre o nó atual e o nó da próxima coluna
                        self.G.add_edge((i, j), (i, j + 1), weight=self.matrix[i, j + 1])
                    if i + 1 < rows and self.matrix[i + 1, j] != 0:  # Se a próxima linha não for água
                        # Adiciona a aresta entre o nó atual e o nó da próxima linha
                        self.G.add_edge((i, j), (i + 1, j), weight=self.matrix[i + 1, j])

    def calculate_heuristic(self, goal):
        """
        Calcula a heurística para cada nó do grafo, a Heuristica é a distancia do nó até o objetivo + a quantidade de água/parade no caminho
        com um incremento de 1.1 caso o caminho não seja promissor (isso ajuda a evitar caminhos que não levam ao objetivo porem tem heurística menor)
        :param goal: objetivo
        :return: Se o objetivo está no grafo
        """

        # Se o objetivo não está no grafo ou não tem vizinhos retorna falso
        if goal not in self.G.nodes() or list(self.G.neighbors(goal)) == []:
            return False

        # Calcula a heurística para cada nó
        for node in self.G.nodes():
            i, j = node  # Pega a linha e a coluna do nó

            rows_water = 0  # Contador de linhas de água/parade ate o objetivo
            cols_water = 0  # Contador de colunas de água/parade ate o objetivo

            # Caso o objetivo esteja acima ou abaixo do nó atual, inverte a ordem para percorrer
            initial_row, final_row = min(i, goal[0]), max(i, goal[0])
            for row in range(initial_row, final_row + 1):  # Para cada linha até o objetivo
                if self.matrix[row, j] == 0:  # Se a linha for água/parade
                    rows_water += 1  # Incrementa o contador

            # Caso o objetivo esteja a esquerda ou a direita do nó atual, inverte a ordem para percorrer
            initial_col, final_col = min(j, goal[1]), max(j, goal[1])
            for col in range(initial_col, final_col + 1):  # Para cada coluna até o objetivo
                if self.matrix[i, col] == 0:  # Se a coluna for água/parade
                    cols_water += 1  # Incrementa o contador

            # Calcula a heurística para o nó
            heuristic = (abs(i - goal[0]) + rows_water / 2) + (abs(j - goal[1]) + cols_water / 2)

            # Se o nó for moeda decrementa a heurística
            if self.matrix[i, j] == -100:
                heuristic -= 2

            self.G.nodes[node]['heuristic_ini'] = heuristic  # Armazena a heurística inicial

        # Segunda etapa para calcular a heurística final
        for node in self.G.nodes():

            heuristic_ini = self.G.nodes[node]['heuristic_ini']  # Pega a heurística inicial

            # Se o nó for o objetivo, a heurística final é a inicial
            if node == goal:
                self.G.nodes[node]['heuristic'] = heuristic_ini
                continue

            neighbor_best = False  # Flag para verificar se o vizinho tem heurística melhor
            for neighbor in self.G.neighbors(node):  # Para cada vizinho do nó
                heuristic_neighbor = self.G.nodes[neighbor]['heuristic_ini']  # Pega a heurística inicial do vizinho
                if heuristic_ini > heuristic_neighbor:  # Se a heurística inicial do nó for maior que a do vizinho
                    neighbor_best = True  # O vizinho tem heurística melhor, ou seja o caminho é promissor

            if neighbor_best:
                self.G.nodes[node][
                    'heuristic'] = heuristic_ini  # Se o vizinho tem heurística melhor, a heurística final é a inicial
            else:
                self.G.nodes[node][
                    'heuristic'] = heuristic_ini + 1.1  # Se o vizinho não tem heurística melhor, incrementa a heurística pois o caminho não é promissor

        return True  # Retorna verdadeiro pois o objetivo está no grafo e é possivel chegar a ele a partir do nó inicial
