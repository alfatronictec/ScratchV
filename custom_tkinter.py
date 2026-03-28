import os
import sys
import time
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

idioma = "pt"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ===============================
# Configuração do tema
# ===============================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ===============================
# Criação da janela
# ===============================
janela = ctk.CTk()
janela.title("ScratchV")
janela.iconbitmap(resource_path("icon.ico"))
janela.geometry("700x400")
janela.minsize(500, 250)
janela.maxsize(900, 600)
janela.resizable(True, True)

# ===============================
# Funções de idioma
# ===============================

def carregar_bandeira(path, size=(30, 20)):
    img = Image.open(resource_path(path)).resize(size)

    colorida = ImageTk.PhotoImage(img)

    cinza = ImageEnhance.Color(img).enhance(0.0)
    cinza = ImageTk.PhotoImage(cinza)

    return colorida, cinza


def selecionar_idioma(novo):
    global idioma
    idioma = novo
    atualizar_botoes_idioma()
    print("Idioma:", idioma)


def atualizar_botoes_idioma():
    if idioma == "pt":
        botao_br.configure(image=img_br_color)
        botao_en.configure(image=img_en_gray)
        botao_cn.configure(image=img_cn_gray)

    elif idioma == "en":
        botao_br.configure(image=img_br_gray)
        botao_en.configure(image=img_en_color)
        botao_cn.configure(image=img_cn_gray)

    elif idioma == "cn":
        botao_br.configure(image=img_br_gray)
        botao_en.configure(image=img_en_gray)
        botao_cn.configure(image=img_cn_color)

# ===============================
# Funções dos botões
# ===============================

def carregar_zip():
    arquivo_zip = filedialog.askopenfilename(
        title="Selecione um arquivo .sb3",
        filetypes=[("Arquivos Scratch", "*.sb3")]
    )

    if not arquivo_zip:
        return
    
    pasta_app = os.path.join(os.path.expanduser("~"), "Documents", "app_teste")
    os.makedirs(pasta_app, exist_ok=True)
    
    for i in range(101):
        barra_progresso.set(i/100)
        janela.update()
        time.sleep(0.01)
    
    print(f"Arquivo carregado: {arquivo_zip}")


def gerar_txt():
    pasta_app = os.path.join(os.path.expanduser("~"), "Documents", "app_teste")
    os.makedirs(pasta_app, exist_ok=True)
    
    arquivo_txt = os.path.join(pasta_app, "saida.txt")

    with open(arquivo_txt, "w") as f:
        f.write("Botão clicado")
    
    print(f"Arquivo criado: {arquivo_txt}")

# ===============================
# Frame central
# ===============================
frame_central = ctk.CTkFrame(janela, fg_color="transparent")
frame_central.pack(expand=True, fill="both")

# ===============================
# Fundo
# ===============================
imagem_original = Image.open(resource_path("plano_fundo.jpeg")).convert("RGBA")
alpha = 0.3
imagem_transparente = Image.blend(imagem_original, Image.new("RGBA", imagem_original.size), 1 - alpha)

bg_image_tk = ImageTk.PhotoImage(imagem_transparente)

label_fundo = ctk.CTkLabel(frame_central, image=bg_image_tk, text="")
label_fundo.place(relx=0.5, rely=0.5, anchor="center")

def atualizar_fundo(event):
    largura = event.width
    altura = event.height

    img = imagem_transparente.resize((largura, altura), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    label_fundo.configure(image=img_tk)
    label_fundo.image = img_tk

frame_central.bind("<Configure>", atualizar_fundo)

# ===============================
# BARRA + BOTÃO
# ===============================
barra_progresso = ctk.CTkProgressBar(frame_central, width=400)
barra_progresso.place(relx=0.5, rely=0.3, anchor="center")
barra_progresso.set(0)

botao_zip = ctk.CTkButton(
    frame_central,
    text="Carregar .sb3",
    command=carregar_zip,

    fg_color="#f7e714",       # cor do botão
    hover_color="#E98512",    # cor ao passar o mouse
    text_color="black"          # cor do texto
)

botao_zip.place(relx=0.5, rely=0.45, anchor="center")

# ===============================
# BOTÕES DE IDIOMA (TOPO DIREITO)
# ===============================

frame_topo = ctk.CTkFrame(frame_central, fg_color="transparent")
frame_topo.place(relx=1.0, rely=0.0, anchor="ne")

# carregar imagens
img_br_color, img_br_gray = carregar_bandeira("br.png")
img_en_color, img_en_gray = carregar_bandeira("us.png")
img_cn_color, img_cn_gray = carregar_bandeira("cn.png")

botao_br = ctk.CTkButton(
    frame_topo, text="", image=img_br_color,
    width=40, fg_color="transparent", hover=False,
    command=lambda: selecionar_idioma("pt")
)
botao_br.pack(side="left", padx=5, pady=5)

botao_en = ctk.CTkButton(
    frame_topo, text="", image=img_en_gray,
    width=40, fg_color="transparent", hover=False,
    command=lambda: selecionar_idioma("en")
)
botao_en.pack(side="left", padx=5, pady=5)

botao_cn = ctk.CTkButton(
    frame_topo, text="", image=img_cn_gray,
    width=40, fg_color="transparent", hover=False,
    command=lambda: selecionar_idioma("cn")
)
botao_cn.pack(side="left", padx=5, pady=5)

# estado inicial
atualizar_botoes_idioma()

# ===============================
# Executa
# ===============================
janela.mainloop()