import time
from algoritmos.busca_gulosa import Gulosa
from algoritmos.busca_a import A_star
from algoritmos.busca_largura import Largura
from algoritmos.busca_profundidade import Profundidade


class Relatorio:

    def __init__(self, graph, start, goal):
        """
        Classe que gera o relatório de comparação dos algoritmos
        :param graph: Grafo do mapa
        :param start: nó inicial
        :param goal: nó objetivo
        """
        self.graph = graph
        self.start = start
        self.goal = goal

        self.gulosa = Gulosa(self.graph, (0, 0), self.goal)
        self.a_star = A_star(self.graph, (0, 0), self.goal)
        self.largura = Largura(self.graph.G, (0, 0), self.goal)
        self.profundidade = Profundidade(self.graph.G, (0, 0), self.goal)

    def calcular_custos(self, path):
        """
        Calcula o custo do caminho encontrado
        :param path: caminho
        :return: custo
        """
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph.G[path[i]][path[i + 1]]['weight']
        return cost

    def gerar_relatorio(self):
        """
        Gera o relatório de comparação dos algoritmos
        :return: relatório de comparação dos algoritmos em formato de string
        """

        # Executa os algoritmos e calcula o tempo de execução, nós visitados, custo e caminho encontrado
        start_time = time.perf_counter()
        self.gulosa.search()
        gulosa_time = time.perf_counter() - start_time
        gulosa_path = self.gulosa.path
        gulosa_nos_visitados = len(self.gulosa.path)

        start_time = time.perf_counter()
        self.a_star.search()
        a_star_time = time.perf_counter() - start_time
        a_star_path = self.a_star.best_path()
        a_star_nos_visitados = len(self.a_star.path)

        start_time = time.perf_counter()
        self.largura.search()
        largura_time = time.perf_counter() - start_time
        largura_path = self.largura.best_path()
        largura_nos_visitados = len(self.largura.path)

        start_time = time.perf_counter()
        self.profundidade.search()
        profundidade_time = time.perf_counter() - start_time
        profundidade_path = self.profundidade.best_path()
        profundidade_nos_visitados = len(self.profundidade.path)

        relatorio = f"""
        RELATÓRIO DE COMPARAÇÃO DOS ALGORITMOS:
        =======================================
        1. Gulosa
           - Tempo de execução: {gulosa_time:.8f} segundos
           - Nós visitados: {gulosa_nos_visitados}
           - Custo: {self.calcular_custos(gulosa_path)}
           - Caminho encontrado: {gulosa_path}

    
        2. A*
           - Tempo de execução: {a_star_time:.8f} segundos
           - Nós visitados: {a_star_nos_visitados}
           - Custo: {self.calcular_custos(a_star_path)}
           - Caminho encontrado: {a_star_path}

    
        3. Largura
           - Tempo de execução: {largura_time:.8f} segundos
           - Nós visitados: {largura_nos_visitados}
           - Custo: {self.calcular_custos(largura_path)}
           - Caminho encontrado: {largura_path}
    
        4. Profundidade
           - Tempo de execução: {profundidade_time:.8f} segundos
           - Nós visitados: {profundidade_nos_visitados}
           - Custo: {self.calcular_custos(profundidade_path)}
           - Caminho encontrado: {profundidade_path}
        """
        return relatorio
