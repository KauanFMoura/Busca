import numpy as np
from tkinter import messagebox
from interfaces.interface import Interface
from graph import Graph
from interfaces.graph_animation import Animation_graph
from algoritmos.busca_gulosa import Gulosa
from algoritmos.busca_a import A_star
from algoritmos.busca_largura import Largura
from algoritmos.busca_profundidade import Profundidade
from interfaces.interface_relatorio import InterfaceRelatorio

if __name__ == "__main__":

    # Carregar o mapa
    matrix = np.loadtxt('mapa.txt', dtype=int)

    # Criar a interface
    gui = Interface(matrix)
    gui.red_image() # Redimensionar as imagens
    gui.create_gui()

    goal = gui.goal # Objetivo escolhido pelo usuário

    # Criar o grafo
    graph = Graph(matrix)
    graph.create_graph()
    in_graph = graph.calculate_heuristic(goal) # Calcular a heurística para o objetivo

    if not in_graph:
        messagebox.showerror("Erro", "Impossivel chegar no Objetivo!")
        exit()

    # Executar o algoritmo escolhido
    if gui.selected_algorithm == "Busca Gulosa":
        gulosa = Gulosa(graph, (0, 0), goal)
        gulosa.search()

        animation = Animation_graph(matrix, graph.G, gulosa.path, gulosa.path)
        animation.draw_graph(goal)

    elif gui.selected_algorithm == "A*":
        a_star = A_star(graph, (0, 0), goal)
        a_star.search()

        animation = Animation_graph(matrix, graph.G, a_star.path, a_star.best_path())
        animation.draw_graph(goal)

    elif gui.selected_algorithm == "Busca em Largura":
        largura = Largura(graph.G, (0, 0), goal)
        largura.search()

        animation = Animation_graph(matrix, graph.G, largura.path, largura.best_path())
        animation.draw_graph(goal)

    elif gui.selected_algorithm == "Busca em Profundidade":
        profundidade = Profundidade(graph.G, (0, 0), goal)
        profundidade.search()

        animation = Animation_graph(matrix, graph.G, profundidade.path, profundidade.best_path())
        animation.draw_graph(goal)

    elif gui.selected_algorithm == "Gerar Relatório":
        relatorio = InterfaceRelatorio()
        relatorio.exibir_relatorio(graph, (0, 0), goal)



