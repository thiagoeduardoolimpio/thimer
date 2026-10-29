import tkinter as tk

tempo_restante = 60

def iniciar_timer():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1

        texto.config(text=f"{tempo_restante:02d}")

        janela.after(1000, iniciar_timer)

janela = tk.Tk()
janela.title("Thimer :p")
janela.geometry("400x350")

texto = tk.Label(janela, text="00:00", font=("Arial", 40))
texto.pack(paddy=20)

botao = tk.Button(janela, text="Iniciar")
botao.pack()

janela.mainloop()





