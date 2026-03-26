import os
import sys
import time
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ===============================
# Configuração do tema
# ===============================
ctk.set_appearance_mode("dark")   # modo dark
ctk.set_default_color_theme("blue")  # tema de cores

# ===============================
# Criação da janela
# ===============================
janela = ctk.CTk()
janela.title("ScratchV")

# define o ícone da janela
janela.iconbitmap(resource_path("icon.ico"))

# tamanho inicial da janela
janela.geometry("700x400")

# tamanho mínimo permitido
janela.minsize(500, 250)

# tamanho máximo permitido
janela.maxsize(900, 600)

# permite redimensionar a janela
janela.resizable(True, True)

# ===============================
# Funções dos botões
# ===============================

def carregar_zip():
    # abre seletor de arquivos filtrando apenas .zip
    arquivo_zip = filedialog.askopenfilename(
        title="Selecione um arquivo .zip",
        #filetypes=[("Arquivos ZIP", "*.zip","*.sb3")]
        filetypes=[("Arquivos ZIP", "*.sb3")]

    )

    # se cancelar, sai da função
    if not arquivo_zip:
        return
    
    # cria pasta Documents/app_teste se não existir
    pasta_app = os.path.join(os.path.expanduser("~"), "Documents", "app_teste")
    os.makedirs(pasta_app, exist_ok=True)
    
    # simulação de carregamento na barra de progresso
    for i in range(101):
        barra_progresso.set(i/100)
        janela.update()
        time.sleep(0.01)
    
    print(f"Arquivo .zip carregado: {arquivo_zip}")


def gerar_txt():
    # cria pasta Documents/app_teste
    pasta_app = os.path.join(os.path.expanduser("~"), "Documents", "app_teste")
    os.makedirs(pasta_app, exist_ok=True)
    
    # cria o arquivo txt
    arquivo_txt = os.path.join(pasta_app, "saida.txt")

    with open(arquivo_txt, "w") as f:
        f.write("Botão clicado")
    
    print(f"Arquivo .txt criado em: {arquivo_txt}")


# ===============================
# Frame central
# ===============================

# frame que ocupa toda a janela
frame_central = ctk.CTkFrame(janela, fg_color="transparent")
frame_central.pack(expand=True, fill="both")


# ===============================
# Carregando a imagem de fundo
# ===============================

# abre a imagem
imagem_original = Image.open("plano_fundo.jpeg").convert("RGBA")

# nível de transparência
alpha = 0.3

# cria nova imagem transparente
imagem_transparente = Image.new("RGBA", imagem_original.size)

# mistura as imagens para criar transparência
imagem_transparente = Image.blend(imagem_original, imagem_transparente, 1 - alpha)

# cria objeto usado pelo tkinter
bg_image_tk = ImageTk.PhotoImage(imagem_transparente)

# label que contém a imagem
label_fundo = ctk.CTkLabel(frame_central, image=bg_image_tk, text="")

# posiciona a imagem no centro
label_fundo.place(relx=0.5, rely=0.5, anchor="center")


# ===============================
# Redimensionamento da imagem
# ===============================

def atualizar_fundo(event):

    largura = event.width
    altura = event.height

    # redimensiona imagem para tamanho da janela
    imagem_redimensionada = imagem_transparente.resize((largura, altura), Image.Resampling.LANCZOS)

    bg_image_tk2 = ImageTk.PhotoImage(imagem_redimensionada)

    # atualiza a imagem no label
    label_fundo.configure(image=bg_image_tk2)

    # mantém referência para não ser apagada pelo GC
    label_fundo.image = bg_image_tk2


# evento chamado quando a janela muda de tamanho
frame_central.bind("<Configure>", atualizar_fundo)


# ===============================
# Barra de progresso e botões
# ===============================

# barra de progresso
barra_progresso = ctk.CTkProgressBar(frame_central, width=400)

# posição da barra
# relx = posição horizontal
# rely = posição vertical
barra_progresso.place(relx=0.5, rely=0.3, anchor="center")

barra_progresso.set(0)


# botão para carregar zip
botao_zip = ctk.CTkButton(
    frame_central,
    text="Carregar .sb3",
    command=carregar_zip
)

# posição do botão
botao_zip.place(relx=0.5, rely=0.45, anchor="center")


# botão para gerar txt
#botao_txt = ctk.CTkButton(
#    frame_central,
#    text="Gerar .txt",
#    command=gerar_txt
#)

# posição do botão
#botao_txt.place(relx=0.5, rely=0.6, anchor="center")


# ===============================
# Executa a janela
# ===============================
janela.mainloop()