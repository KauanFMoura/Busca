import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation


class Animation_graph:

        def __init__(self, matrix, G, path, best_path):
            """
            Classe que gera a animação de busca no grafo
            :param matrix: matriz do mapa
            :param G: grafo do mapa
            :param path: nos visitados
            :param best_path: caminho final
            """
            self.matrix = matrix
            self.G = G
            self.path = path
            self.best_path = best_path
            self.visited_nodes = []
            self.root = tk.Tk()
            self.fig, self.ax = plt.subplots(figsize=(12, 8))
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.canvas.get_tk_widget().pack()

        def draw_graph(self, goal):
            """
            Desenha o gráfico
            :param goal: nó objetivo
            :return:
            """

            rows, cols = self.matrix.shape # Pega o tamanho da matriz
            pos = {(i, j): (j, -i) for i in range(rows) for j in range(cols) if self.matrix[i, j] != 0} # Posição dos nós
            node_labels = {node: f"{node}\nH:{self.G.nodes[node]['heuristic']:.2f}" for node in self.G.nodes()} # Labels dos nós

            # Pega os nós com moedas, para desenhar de outra cor
            coin_node = []
            for i in range(rows):
                for j in range(cols):
                    if self.matrix[i, j] == -100:
                        coin_node.append((i, j))

            def update(frame):
                """
                Atualiza o gráfico a cada frame da animação
                :param frame: frame atual
                :return:
                """

                # Limpar o gráfico para evitar sobreposição
                self.ax.clear()

                # elementos fixos
                nx.draw(self.G, pos, ax=self.ax, with_labels=False, node_color="lightblue", edge_color="gray", node_size=500)
                nx.draw_networkx_labels(self.G, pos, labels=node_labels, font_size=6, font_color="black")
                nx.draw_networkx_nodes(self.G, pos, ax=self.ax, nodelist=coin_node, node_color="yellow", node_size=500)
                nx.draw_networkx_nodes(self.G, pos, ax=self.ax, nodelist=[goal], node_color="purple", node_size=400)

                # Verificar se a animação chegou ao fim
                if frame >= len(self.path):
                    # Verfica se o objetivo foi alcançado
                    message = "Objetivo alcançado!" if goal in self.best_path else "Objetivo não alcançado."

                    # Pinta os nós do caminho final de vermelho
                    nx.draw_networkx_nodes(self.G, pos, ax=self.ax, nodelist=self.best_path, node_color="red")
                    self.ax.set_title(message)
                    ani.event_source.stop() # Parar a animação
                    return

                # Atualizar os nós visitados
                current_node = self.path[frame] # Nó atual
                if current_node not in self.visited_nodes: # Se o nó não foi visitado, adiciona na lista (evita repetição)
                    self.visited_nodes.append(current_node)

                # Atualizar nós visitados (verde)
                nx.draw_networkx_nodes(self.G, pos, ax=self.ax, nodelist=self.visited_nodes, node_color="green")
                # Atualizar o nó atual (vermelho)
                nx.draw_networkx_nodes(self.G, pos, ax=self.ax, nodelist=[current_node], node_color="red")

                # Atualizar título
                self.ax.set_title(f"Passo {frame + 1}: Visitando {current_node}")

            # Configurar animação
            ani = animation.FuncAnimation(self.fig, update, frames=len(self.path) + 1, interval=1, repeat=False)

            # Executar a interface
            self.root.eval('tk::PlaceWindow . center')
            self.root.mainloop()

