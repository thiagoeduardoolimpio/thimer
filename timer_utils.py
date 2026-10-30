from tkinter import messagebox

def atualizar_tempo(texto, janela, tempo_restante, optionmenu):
    if tempo_restante > 0:
        tempo_restante -= 1
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60
        texto.config(text=f"{minutos:02d}:{segundos:02d}")
        
        # Passamos os argumentos para a próxima execução do after
        timer_id = janela.after(1000, atualizar_tempo, texto, janela, tempo_restante, optionmenu)
        return timer_id, tempo_restante
    else:
        mostrar_aviso()
        optionmenu.configure(state="normal")
        return None, 0

def iniciar_timer(janela, timer_id):
    if timer_id is not None:
        janela.after_cancel(timer_id)


def converterMinutos(minutos):
    time = minutos * 60
    return time
    # depois eu passaria tipo assim pra imprimir o valor correto... -> print(f"{minutos}:{segundos}")

def mostrar_aviso():
    messagebox.showinfo("Alerta:", "Timer chegou ao fim. Inicie outro foco")
    
#def formatar_tempo(segundos):

    # função para formatar 60 em 01:00

    #minutos = segundos // 60
    #segs = segundos % 60
    #return f"{minutos:02d}:{segs:02d}"  