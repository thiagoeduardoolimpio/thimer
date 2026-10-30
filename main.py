import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import timer_utils

tempo_restante = 0 
tempoTimer_escolhido = 0
timer_id = None

def optionmenu_callback(choice):
    print("minutos:", choice)

    global tempoTimer_escolhido 
    tempoTimer_escolhido = int(choice)
    texto.config(text=choice)
    return tempoTimer_escolhido

def iniciar():
    global tempo_restante, timer_id, tempoTimer_escolhido
    
    # Cancela o timer anterior se existir
    timer_utils.iniciar_timer(janela, timer_id)
    optionmenu.configure(state="disabled")
    tempo_restante = timer_utils.converterMinutos(tempoTimer_escolhido)

    # Inicia a contagem passando os parâmetros
    timer_id, tempo_restante = timer_utils.atualizar_tempo(texto, janela, tempo_restante, optionmenu)

janela = tk.Tk()
janela.title("Hello user!   :p")
janela.geometry("505x400")

# codigo da logo
try:
    icone = tk.PhotoImage(file="assets/icontemp.png")
    janela.iconphoto(True, icone)
except Exception as e:
    print(f"Erro ao carregar o ícone: {e}")

texto = tk.Label(janela, text=tempoTimer_escolhido, font=("Arial", 100))

texto.pack(pady=40)

# menu de escolhas 
optionmenu_var = ctk.StringVar(value="option 2")
optionmenu = ctk.CTkOptionMenu(janela,values=["0","1","2","10", "15", "20", "25", "30", "35", "40", "45"],
    command=optionmenu_callback
    #variable=optionmenu_var
    )

optionmenu.pack(pady=10)

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