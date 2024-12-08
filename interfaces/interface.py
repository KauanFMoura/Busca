import tkinter as tk
from tkinter import PhotoImage, messagebox


class Interface:
    # Mapeamento de valores para imagens
    IMAGE_MAP = {
        0: "imgs/water.png",
        1: "imgs/grass.png",
        10: "imgs/stone.png",
        4: "imgs/sand.png",
        20: "imgs/dirty.png",
        -100: "imgs/coin.png",
        3: "imgs/hero.png",
    }

    def __init__(self, matrix, block_size=(60, 60)):
        """
        Classe que cria a interface gráfica
        :param matrix: matriz do mapa
        :param block_size: tamanho do bloco da imagem (para ficar certo a imagem precisa ser 512x512)
        """
        self.matrix = matrix
        self.block_size = block_size
        self.root = tk.Tk()
        self.images = {}
        self.goal = None
        self.selected_algorithm = None

    def red_image(self):
        """Redimensiona as imagens para o tamanho do bloco
        :return
        """
        for key, value in self.IMAGE_MAP.items():
            image = PhotoImage(file=value)
            image = image.subsample(int(image.width() / self.block_size[0]), int(image.height() / self.block_size[1]))
            self.images[key] = image

    def on_click(self, event):
        """
        Função chamada quando um bloco é clicado
        :param event: evento do clique
        :return:
        """
        # Usando grid_info() para obter a linha e a coluna do clique
        label_info = event.widget.grid_info()
        row = label_info['row']
        col = label_info['column']
        self.goal = (row, col)  # Define o objetivo

        # Chama o popup para escolher o algoritmo
        self.select_algoritmo()

    def on_hover_enter(self, event):
        """Destaca o bloco quando o mouse entra sobre ele
        :param event: evento do hover
        :return:
        """
        event.widget.config(borderwidth=2, relief="solid", bg="yellow", padx=1, pady=1)

    def on_hover_leave(self, event):
        """Remove o destaque quando o mouse sai
        :param event: evento do hover
        :return:
        """
        event.widget.config(borderwidth=0, relief="flat", padx=0, pady=0)

    def select_algoritmo(self):
        """Abre um popup para o usuário escolher o algoritmo de busca
        :return:
        """

        # Cria uma nova janela de popup
        popup = tk.Toplevel(self.root)
        popup.geometry("300x250")  # Define o tamanho da janela do popup

        # Lista de algoritmos
        algorithms = ["Busca Gulosa", "A*", "Busca em Largura", "Busca em Profundidade", "Gerar Relatório"]

        # Criação de uma variável para armazenar a escolha
        algoritmo_choice = tk.StringVar(popup)
        algoritmo_choice.set(algorithms[0])  # Valor inicial

        # Título do popup
        label = tk.Label(popup, text="Escolha o Algoritmo de Busca:")
        label.pack(pady=10)

        # Criação das opções para selecionar o algoritmo
        for algorithm in algorithms:
            radio_button = tk.Radiobutton(popup, text=algorithm, variable=algoritmo_choice, value=algorithm)
            radio_button.pack(anchor="w")

        def on_confirm():
            """Função chamada quando o botão "Confirmar" é clicado
            :return:
            """

            self.selected_algorithm = algoritmo_choice.get()  # Define o algoritmo selecionado
            # Mostra uma mensagem com o algoritmo selecionado
            messagebox.showinfo("Aviso!",
                                f"Algoritmo Selecionado: {self.selected_algorithm} para o objetivo {self.goal}")
            popup.destroy()  # Fecha o popup
            self.root.destroy()  # Fecha a janela principal

        # Botão de confirmação
        confirm_button = tk.Button(popup, text="Confirmar", command=on_confirm)
        confirm_button.pack(pady=20)

    def create_gui(self):
        """Cria a interface gráfica
        :return:
        """

        rows = len(self.matrix)  # Número de linhas
        cols = len(self.matrix[0])  # Número de colunas

        for i in range(rows):  # Loop pelas linhas
            for j in range(cols):  # Loop pelas colunas
                value = self.matrix[i][j]  # Valor do bloco
                image = self.images.get(value)  # Imagem do bloco atual com base no valor da matriz
                # Cria um label com a imagem do bloco
                label = tk.Label(self.root, image=image, width=self.block_size[0], height=self.block_size[1])
                label.image = image  # Salva a imagem
                label.grid(row=i, column=j, padx=0, pady=0)  # Posiciona o label na janela
                label.grid(row=i, column=j, sticky="nsew")  # Define o alinhamento

                # Associa a ação de clique a cada label
                label.bind("<Button-1>", self.on_click)

                # Associa eventos de hover
                label.bind("<Enter>", self.on_hover_enter)
                label.bind("<Leave>", self.on_hover_leave)

        # Centraliza a janela
        self.root.eval('tk::PlaceWindow . center')
        self.root.mainloop()  # Executa a interface
