import tkinter as tk
from tkinter import messagebox
import timer_utils
tempo_restante = 60
timer_id = None
  
def iniciar():
    global tempo_restante, timer_id
    
    # Cancela o timer anterior se existir
    timer_utils.iniciar_timer(janela, timer_id)
    
    tempo_restante = 60
    # Inicia a contagem passando os parâmetros
    timer_id, tempo_restante = timer_utils.atualizar_tempo(texto, janela, tempo_restante)


janela = tk.Tk()
janela.title("Thimer :p")
janela.geometry("180x160")

# codigo da logo (teste)
try:
    icone = tk.PhotoImage(file="assets/icontemp.png")
    janela.iconphoto(True, icone)
except Exception as e:
    print(f"Erro ao carregar o ícone: {e}")

texto = tk.Label(janela, text="60", font=("Arial", 40))
texto.pack(pady=20)

botao = tk.Button(janela, text="Inicio", command=iniciar)
botao.pack()

janela.mainloop()





