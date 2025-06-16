import tkinter as tk
from tkinter import messagebox
from minimax_AI import mejor_movimiento_arbol
from classes import Node

class TicTacToeCanvasApp:
    def __init__(self, root, jugador_humano):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
        self.canvas.pack()
        self.jugador_humano = jugador_humano
        self.jugador_ia = 'O' if jugador_humano == 'X' else 'X'
        self.turno = 'X'
        self.tablero = [' ' for _ in range(9)]
        self.dibujar_tablero()
        self.canvas.bind("<Button-1>", self.clic)

        if self.turno == self.jugador_ia:
            self.movimiento_ia()

    def dibujar_tablero(self):
        for i in range(1, 3):
            self.canvas.create_line(100 * i, 0, 100 * i, 300, fill="white", width=4)
            self.canvas.create_line(0, 100 * i, 300, 100 * i, fill="white", width=4)

    def clic(self, evento):
        fila = evento.y // 100
        columna = evento.x // 100
        i = fila * 3 + columna
        if self.tablero[i] == ' ' and self.turno == self.jugador_humano:
            self.tablero[i] = self.jugador_humano
            self.dibujar_simbolo(fila, columna, self.jugador_humano)
            if self.comprobar_fin():
                return
            self.turno = self.jugador_ia
            self.root.after(500, self.movimiento_ia)

    def movimiento_ia(self):
        mov = mejor_movimiento_arbol(self.tablero, self.jugador_ia)
        if mov is not None:
            self.tablero[mov] = self.jugador_ia
            fila, columna = divmod(mov, 3)
            self.dibujar_simbolo(fila, columna, self.jugador_ia)
        if not self.comprobar_fin():
            self.turno = self.jugador_humano

    def dibujar_simbolo(self, fila, columna, simbolo):
        x = columna * 100 + 50
        y = fila * 100 + 50
        if simbolo == 'X':
            self.canvas.create_line(x - 30, y - 30, x + 30, y + 30, fill="blue", width=6)
            self.canvas.create_line(x + 30, y - 30, x - 30, y + 30, fill="blue", width=6)
        else:
            self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, outline="deeppink", width=6)

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
        root.title("Tic Tac Toe con IA")
        app = TicTacToeCanvasApp(root, j)
        root.mainloop()

    menu = tk.Tk()
    menu.title("Selecciona tu ficha")
    menu.configure(bg="black")
    tk.Label(menu, text="¿Con qué ficha quieres jugar?", font=("Arial", 14), bg="black", fg="white").pack(pady=10)
    tk.Button(menu, text="X", font=("Arial", 12), width=10, command=lambda: seleccionar_jugador('X')).pack(pady=5)
    tk.Button(menu, text="O", font=("Arial", 12), width=10, command=lambda: seleccionar_jugador('O')).pack(pady=5)
    menu.mainloop()

if __name__ == '__main__':
    iniciar_juego()
