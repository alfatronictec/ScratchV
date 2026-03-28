# FAZ OPERAÇÕES BÁSICAS DA ISA RISC-V RV32I
# No momento = Soma e Subtração
# No momento = BEQ   if a == b | beq rs1, rs2, label | Se rs1 == rs2, pula para o endereço indicado por label.
# Na sequência fará BLT   if a < b  | blt rs1, rs2, label | Se rs1 < rs2, o programa salta para label.
# Na sequência fará BGT   if a > b  | bgt rs1, rs2, label | Se rs1 > rs2, salta para label
import os
import sys
import time
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
from core import load_sb3, gerar_codigo_python

idioma = "pt"
codigo_python = 0

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
    textos = {
        "pt": "Carregar .sb3",
        "en": "Load .sb3",
        "cn": "加载 .sb3"
    }

    botao_zip.configure(text=textos.get(idioma))

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
    global codigo_python

    arquivo_zip = filedialog.askopenfilename(
        title="Selecione um arquivo .sb3",
        filetypes=[("Arquivos Scratch", "*.sb3")]
    )

    if not arquivo_zip:
        return
    
    project = load_sb3(arquivo_zip)
    codigo_python = gerar_codigo_python(project)

    # GERA O ASSEMBLY
    gerar_assembly(codigo_python)

    for i in range(101):
        barra_progresso.set(i/100)
        janela.update()
        time.sleep(0.01)
    
    print(f"Arquivo carregado: {arquivo_zip}")

    print("\nCODIGO GERADO:\n")
    for linha in codigo_python:
        print(linha)

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

def gerar_assembly(codigo_python):

    reg = 0
    ultimo_reg = None
    registradores = {}
    label_id = 0
    stack_labels = []

    with open("codigo_gerado.asm", "w", encoding="utf-8") as f:

        f.write(".text\n\n")

        for linha in codigo_python:

            if linha.startswith("v="):
                partes = linha.split("=")
                var = partes[1].strip()

                if len(partes) > 2 and partes[2].strip().isdigit():
                    valor = partes[2].strip()
                    
                    if idioma == "pt":
                        f.write(f"   li t{reg}, {valor}                 # Armazena o valor {valor} no registrador t{reg}\n\n")
                    elif idioma == "en":
                        f.write(f"   li t{reg}, {valor}                 # Store the value {valor} in register t{reg}\n\n")
                    elif idioma == "cn":
                        f.write(f"   li t{reg}, {valor}                 # 将值 {valor} 存入寄存器 t{reg}\n\n")
                    registradores[var] = reg
                    ultimo_reg = reg
                    reg += 1
                else:
                    registradores[var] = ultimo_reg
            
            # =========================
            # SOMA
            # =========================
            elif linha.startswith("vr+"):

                var = linha.split("=")[1].strip()
                
                if idioma == "pt":
                    f.write(f"   add t{reg}, t{reg-2}, t{reg-1}   # Soma o valor armazenado em t{reg-1} com o armazenado em t{reg-2} e armazena o resultado no registrador t{reg} \n\n")

                elif idioma == "en":
                    f.write(f"   add t{reg}, t{reg-2}, t{reg-1}   # Add the value stored in t{reg-1} to the value stored in t{reg-2} and store the result in the register t{reg} \n\n")

                elif idioma == "cn":
                    f.write(f"   add t{reg}, t{reg-2}, t{reg-1}   # 将存储在 t{reg-1} 中的值与存储在 t{reg-2} 中的值相加，并将结果存储在寄存器 t{reg} 中 \n\n")

                registradores[var] = reg  

                ultimo_reg = reg
                reg += 1

            # =========================
            # SUBTRAÇÃO
            # =========================
            elif linha.startswith("vr-"):

                var = linha.split("=")[1].strip()
                if idioma == "pt":
                    f.write(f"   sub t{reg}, t{reg-2}, t{reg-1}   # Subtrai o valor armazenado em t{reg-1} do valor armazenado em t{reg-2} e armazena no registrador t{reg} \n\n")
                elif idioma == "en":
                    f.write(f"   sub t{reg}, t{reg-2}, t{reg-1}   # Subtracts the value in t{reg-1} from t{reg-2} and stores the result in t{reg} \n\n")
                elif idioma == "cn":
                    f.write(f"   sub t{reg}, t{reg-2}, t{reg-1}   # 将 t{reg-2} 中的值减去 t{reg-1} 中的值，并将结果存入寄存器 t{reg} \n\n")
                registradores[var] = reg  
                ultimo_reg = reg
                reg += 1

            # =========================
            # PRINT
            # =========================
            elif linha.startswith("p="):

                var = linha.split("=")[1].strip()
                r = registradores[var]
                if idioma == "pt":
                    f.write("   li a7, 1             # Carrega o valor 1 no registrador a7, que define o codigo da syscall (servico do sistema), 1 = imprimir inteiro (print integer) \n")
                    f.write(f"   add a0, t{r}, zero    # Copia o valor do registrador t2 para a0, a0 é o registrador usado para passar o argumento da syscall, o inteiro que será impresso  \n") 
                    f.write("   ecall                # Executa uma chamada de sistema (environment call)\n\n")
                elif idioma == "en":
                    f.write("   li a7, 1             # Loads the value 1 into register a7, which defines the syscall code (system service); 1 = print integer  \n")
                    f.write(f"   add a0, t{r}, zero    # Copies the value from register t2 to a0; a0 is the register used to pass the syscall argument, the integer that will be printed   \n") 
                    f.write("   ecall                # Performs an environment call\n\n")                    
                elif idioma == "cn":
                    f.write("   li a7, 1             # 将值 1 写入寄存器 a7，该值定义了系统调用（syscall）的代码，1 表示“打印整数”（print integer）\n")
                    f.write(f"   add a0, t{r}, zero    # 将寄存器 t2 的值复制到 a0，a0 是用于传递系统调用参数的寄存器，即待输出的整数\n") 
                    f.write("   ecall                # 执行系统调用（environment call）\n\n")
            # =========================
            # IF IGUAL (BEQ)
            # =========================
            elif linha.startswith("i="):

                conteudo = linha[3:]
                var1, var2 = conteudo.split("|")

                r1 = registradores[var1]
                r2 = registradores[var2]

                label_true = f"IF_EQUAL_{label_id}"
                label_end = f"IF_NOT_EQUAL_{label_id}"

                stack_labels.append((label_true, label_end))
                label_id += 1

                f.write(f"   beq t{r1}, t{r2}, {label_true}      # Compara os valores armazenados, se t{r1} = t{r2} pula para {label_true}, se nao continua \n\n")
                f.write(f"   j {label_end}             # Salta para {label_end} \n\n")
            
            # =========================
            # IF MAIOR (BGT)
            # =========================
            elif linha.startswith("i>"):

                conteudo = linha[2:]  # remove "i>"

                var1, var2 = conteudo.split("|")

                r1 = registradores[var1]
                r2 = registradores[var2]

                f.write(f"   bgt t{r1}, t{r2}, MAIOR\n\n")

            # =========================
            # IF MENOR (BLT)
            # =========================
            elif linha.startswith("i<"):

                conteudo = linha[2:]

                var1, var2 = conteudo.split("|")

                r1 = registradores[var1]
                r2 = registradores[var2]

                f.write(f"   blt t{r1}, t{r2}, MENOR\n\n")
            
            elif linha == "IF_START":

                label_true, _ = stack_labels[-1]

                f.write(f"{label_true}:\n")
            
            elif linha == "IF_END":

                _, label_end = stack_labels.pop()

                f.write(f"{label_end}:\n\n")

            else:
                print("Linha não reconhecida:", linha)

# ===============================
# Executa
# ===============================
janela.mainloop()
