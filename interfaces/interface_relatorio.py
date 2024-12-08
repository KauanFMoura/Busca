import tkinter as tk
from tkinter import scrolledtext

from relatorio import Relatorio

class InterfaceRelatorio:

    def __init__(self):
        """
        Classe que exibe o relatório de comparação dos algoritmos
        """

        self.root = tk.Tk()
        self.root.title("Algoritmos de Busca")

    def exibir_relatorio(self, graph, start, goal):
        """
        Exibe o relatório de comparação dos algoritmos
        :param graph: grafo do mapa
        :param start: nó inicial
        :param goal: nó objetivo
        :return:
        """
        relatorio_obj = Relatorio(graph, start, goal) # Cria o objeto relatório
        relatorio = relatorio_obj.gerar_relatorio() # Gera o relatório

        # Cria a área de texto
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=50)
        self.text_area.pack(expand=True, fill=tk.BOTH) # Adiciona a área de texto à janela
        self.text_area.insert(tk.INSERT, relatorio)  # Insere o relatório
        self.text_area.configure(state="disabled")  # Desativa a edição

        self.root.eval('tk::PlaceWindow . center') # Centraliza a janela
        self.root.geometry("1000x800") # Define o tamanho da janela
        self.root.mainloop() # Executa a interface
