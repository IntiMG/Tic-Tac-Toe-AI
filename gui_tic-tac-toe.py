import tkinter as tk
from tkinter import messagebox
from minimax_AI import mejor_movimiento_arbol
from classes import Node

class TicTacToeApp:
    def __init__(self, root, jugador_humano):
        self.root = root
        self.jugador_humano = jugador_humano
        self.jugador_ia = 'O' if jugador_humano == 'X' else 'X'
        self.turno = 'X'
        self.tablero = [' ' for _ in range(9)]
        self.botones = []
        self.construir_interfaz()

        if self.turno == self.jugador_ia:
            self.movimiento_ia()

    def construir_interfaz(self):
        self.root.title("Tic Tac Toe con IA (Minimax)")
        for i in range(9):
            b = tk.Button(self.root, text=' ', font=('Arial', 20), width=5, height=2,
                         command=lambda i=i: self.movimiento_jugador(i))
            b.grid(row=i // 3, column=i % 3)
            self.botones.append(b)

    def movimiento_jugador(self, i):
        if self.tablero[i] == ' ' and self.turno == self.jugador_humano:
            self.tablero[i] = self.jugador_humano
            self.botones[i].config(text=self.jugador_humano, state="disabled")
            if self.comprobar_fin():
                return
            self.turno = self.jugador_ia
            self.movimiento_ia()

    def movimiento_ia(self):
        mov = mejor_movimiento_arbol(self.tablero, self.jugador_ia)
        if mov is not None:
            self.tablero[mov] = self.jugador_ia
            self.botones[mov].config(text=self.jugador_ia, state="disabled")
        if not self.comprobar_fin():
            self.turno = self.jugador_humano

    def comprobar_fin(self):
        if Node(self.tablero, self.turno).ganador(self.turno):
            messagebox.showinfo("Fin del juego", f"¡Ganó {self.turno}!")
            self.root.quit()
            return True
        elif ' ' not in self.tablero:
            messagebox.showinfo("Fin del juego", "Empate")
            self.root.quit()
            return True
        return False


def iniciar_juego():
    def seleccionar_jugador(j):
        menu.destroy()
        root = tk.Tk()
        app = TicTacToeApp(root, j)
        root.mainloop()

    menu = tk.Tk()
    menu.title("Selecciona tu ficha")
    tk.Label(menu, text="¿Con qué ficha quieres jugar?", font=("Arial", 14)).pack(pady=10)
    tk.Button(menu, text="X", font=("Arial", 12), width=10, command=lambda: seleccionar_jugador('X')).pack(pady=5)
    tk.Button(menu, text="O", font=("Arial", 12), width=10, command=lambda: seleccionar_jugador('O')).pack(pady=5)
    menu.mainloop()

if __name__ == '__main__':
    iniciar_juego()