import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
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
janela.title("Hello user!   :p")
janela.geometry("505x400")

# codigo da logo
try:
    icone = tk.PhotoImage(file="assets/icontemp.png")
    janela.iconphoto(True, icone)
except Exception as e:
    print(f"Erro ao carregar o ícone: {e}")

texto = tk.Label(janela, text="60", font=("Arial", 100))
texto.pack(pady=40)

botao = ctk.CTkButton(
    janela,
    text="Iniciar",
    command=iniciar,
# style
    fg_color="gray",
    text_color="black",
    corner_radius=15,
    width=120,
    height=35        
)
botao.pack(pady=10)
janela.mainloop()