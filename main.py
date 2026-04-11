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
janela.iconbitmap(resource_path("images/icon.ico"))
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
def mostrar_erro(msg):
    label_erro.configure(text=msg)

    # remove depois de 3 segundos (3000 ms)
    janela.after(3000, lambda: label_erro.configure(text=""))

def carregar_zip():
    global codigo_python

    try:
        arquivo_zip = filedialog.askopenfilename(
            title="Selecione um arquivo .sb3",
            filetypes=[("Arquivos Scratch", "*.sb3")]
        )

        if not arquivo_zip:
            return
        
        project = load_sb3(arquivo_zip)
        codigo_python = gerar_codigo_python(project)

        gerar_assembly(codigo_python)

        for i in range(101):
            barra_progresso.set(i/100)
            janela.update()
            time.sleep(0.01)
        
        print(f"Arquivo carregado: {arquivo_zip}")

        print("\ GERADO:\n")
        for linha in codigo_python:
            print(linha)

    except KeyError as e:
        mostrar_erro(f"Variável não definida: {e}")

    except Exception as e:
        mostrar_erro(f"Erro interno: {e}")

# ===============================
# Frame central
# ===============================
frame_central = ctk.CTkFrame(janela, fg_color="transparent")
frame_central.pack(expand=True, fill="both")

# ===============================
# Fundo
# ===============================
imagem_original = Image.open(resource_path("images/plano_fundo.jpeg")).convert("RGBA")
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
barra_progresso = ctk.CTkProgressBar(frame_central, width=400, progress_color="#19E912")
barra_progresso.place(relx=0.5, rely=0.3, anchor="center")
barra_progresso.set(0)

botao_zip = ctk.CTkButton(
    frame_central,
    text="Carregar .sb3",
    command=carregar_zip,
    fg_color="#E98512",       # cor do botão
    hover_color="#f7e714",    # cor ao passar o mouse
    text_color="black"          # cor do texto
)

botao_zip.place(relx=0.5, rely=0.45, anchor="center")

label_erro = ctk.CTkLabel(
    frame_central,
    text="",
    text_color="#ff4d4d",
    font=("Arial", 14)
)
label_erro.place(relx=0.5, rely=0.55, anchor="center")

# ===============================
# BOTÕES DE IDIOMA (TOPO DIREITO)
# ===============================

frame_topo = ctk.CTkFrame(frame_central, fg_color="transparent")
frame_topo.place(relx=1.0, rely=0.0, anchor="ne")

# carregar imagens
img_br_color, img_br_gray = carregar_bandeira("images/br.png")
img_en_color, img_en_gray = carregar_bandeira("images/us.png")
img_cn_color, img_cn_gray = carregar_bandeira("images/cn.png")

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

            print(f"[DEBUG LINHA]: '{linha}'")
            
            linha = linha.strip()   # 🔥 CORRETO

            if not linha:
                continue


            if linha.startswith("v="):
                partes = linha.split("=")
                var = partes[1].strip()

                # Verifica se há um valor imediato
                valor = None
                if len(partes) > 2 and partes[2].strip().isdigit():
                    valor = partes[2].strip()

                # Reutiliza registrador se a variável já existir
                if var in registradores:
                    reg_var = registradores[var]
                else:
                    reg_var = reg
                    registradores[var] = reg_var
                    reg += 1

                    if reg > 6:
                        raise Exception(f"Ultrapassou o Número de Variáveis: {linha}")

                ultimo_reg = reg_var

                # Geração do assembly
                if valor is not None:
                    if idioma == "pt":
                        f.write(f"   li t{reg_var}, {valor}                 # Armazena o valor {valor} no registrador t{reg}\n\n")
                    elif idioma == "en":
                        f.write(f"   li t{reg_var}, {valor}                 # Store the value {valor} in register t{reg}\n\n")
                    elif idioma == "cn":
                        f.write(f"   li t{reg_var}, {valor}                 # 将值 {valor} 存入寄存器 t{reg}\n\n")

            # =========================
            # SOMA
            # =========================
            elif linha.startswith("vr+"):
                conteudo = linha.split("=", 1)[1].strip()
                var_dest, op1, op2 = [p.strip() for p in conteudo.split("|")]

                if op1 not in registradores or op2 not in registradores:
                    raise Exception(f"Variável não definida: {linha}")

                r1 = registradores[op1]
                r2 = registradores[op2]

                # Reutiliza registrador do destino
                if var_dest in registradores:
                    reg_dest = registradores[var_dest]
                else:
                    reg_dest = reg
                    registradores[var_dest] = reg_dest
                    reg += 1

                    if reg > 6:
                        raise Exception(f"Ultrapassou o Número de Variáveis: {linha}")
                
                if idioma == "pt":
                    f.write(f"   add t{reg_dest}, t{r1}, t{r2}              # Soma o valor armazenado em t{r1} com o armazenado em t{r2} e armazena o resultado no registrador t{reg_dest} \n\n")
                elif idioma == "en":
                    f.write(f"   add t{reg_dest}, t{r1}, t{r2}              # Soma o valor armazenado em t{r1} com o armazenado em t{r2} e armazena o resultado no registrador t{reg_dest} \n\n")
                elif idioma == "cn":
                    f.write(f"   add t{reg_dest}, t{r1}, t{r2}              # Soma o valor armazenado em t{r1} com o armazenado em t{r2} e armazena o resultado no registrador t{reg_dest} \n\n")
                ultimo_reg = reg_dest
                
            # =========================
            # SUBTRAÇÃO
            # =========================
            elif linha.startswith("vr-"):
                print("DEBUG SUB:", linha)
                conteudo = linha.split("=", 1)[1].strip()

                # Caso 1: formato ideal → var_dest|var1|var2
                if "|" in conteudo:
                    partes = conteudo.split("|")

                    if len(partes) != 3:
                        raise Exception(f"Formato inválido para sub: {linha}")

                    var_dest = partes[0].strip()
                    op1 = partes[1].strip()
                    op2 = partes[2].strip()

                # Caso 2: formato tipo → soma=(var1-var2)
                elif "-" in conteudo:
                    var_dest, expr = conteudo.split("=", 1)
                    var_dest = var_dest.strip()

                    expr = expr.replace("(", "").replace(")", "")
                    op1, op2 = expr.split("-")

                    op1 = op1.strip()
                    op2 = op2.strip()

                else:
                    raise Exception(f"Formato inválido para sub: {linha}")

                # Validação das variáveis de origem
                if op1 not in registradores:
                    raise Exception(f"Variável não definida: {op1}")
                if op2 not in registradores:
                    raise Exception(f"Variável não definida: {op2}")

                r1 = registradores[op1]
                r2 = registradores[op2]

                # 🔹 Reutiliza registrador da variável de destino, se existir
                if var_dest in registradores:
                    reg_dest = registradores[var_dest]
                else:
                    reg_dest = reg
                    registradores[var_dest] = reg_dest
                    reg += 1

                    if reg > 6:
                        raise Exception(f"Ultrapassou o Número de Variáveis: {linha}")

                # Geração do assembly
                if idioma == "pt":
                    f.write(f"   sub t{reg_dest}, t{r1}, t{r2}              # Subtrai o valor armazenado em t{r1} do valor armazenado em t{r2} e armazena no registrador t{reg_dest} \n\n")
                elif idioma == "en":
                    f.write(f"   sub t{reg_dest}, t{r1}, t{r2}              # Subtrai o valor armazenado em t{r1} do valor armazenado em t{r2} e armazena no registrador t{reg_dest} \n\n")
                elif idioma == "cn":
                    f.write(f"   sub t{reg_dest}, t{r1}, t{r2}              # Subtrai o valor armazenado em t{r1} do valor armazenado em t{r2} e armazena no registrador t{reg_dest} \n\n")

                ultimo_reg = reg_dest
            
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
            elif linha.startswith("i=="):

                # Remove o prefixo 'i=='
                conteudo = linha[len("i=="):].strip()

                try:
                    var1, var2 = [v.strip() for v in conteudo.split("|")]
                except ValueError:
                    raise Exception(f"Formato inválido para igualdade: {linha}")

                print("DEBUG IF:", var1, var2)

                # Validação
                if var1 not in registradores:
                    raise Exception(f"Variável não definida: {var1}")
                if var2 not in registradores:
                    raise Exception(f"Variável não definida: {var2}")

                r1 = registradores[var1]
                r2 = registradores[var2]

                # Criação de labels
                if idioma == "pt":
                    label_true = f"SE_IGUAL_{label_id}"
                    label_end = f"FIM_SE_{label_id}"
                else:
                    label_true = f"IF_EQUAL_{label_id}"
                    label_end = f"IF_END_{label_id}"

                # Armazena apenas TRUE e END
                stack_labels.append((label_true, label_end))
                label_id += 1

                # Estrutura de um IF sem ELSE
                f.write(
                    f"   beq t{r1}, t{r2}, {label_true}      "
                    f"# Se {var1} == {var2}, pula para {label_true}\n"
                )
                f.write(
                    f"   j {label_end}                       "
                    f"# Caso contrário, pula para {label_end}\n\n"
                )
            # =========================
            # IF MAIOR (BGT)
            # =========================
            elif linha.startswith("i>"):
                conteudo = linha.split("=", 1)[1]
                var1, var2 = conteudo.split("|")

                r1 = registradores[var1.strip()]
                r2 = registradores[var2.strip()]

                label_true = f"IF_TRUE_{label_id}"
                label_else = f"IF_FALSE_{label_id}"
                label_end = f"IF_END_{label_id}"

                stack_labels.append((label_true, label_else, label_end))
                label_id += 1

                f.write(f"   bgt t{r1}, t{r2}, {label_true}\n")
                f.write(f"   j {label_else}\n\n")

            # =========================
            # IF MENOR (BLT)
            # =========================
            elif linha.startswith("i<"):

                conteudo = linha.split("=", 1)[1]
                var1, var2 = conteudo.split("|")

                if var1.isdigit():
                    print("i< var1 Erro: IF não aceita valor imediato, use uma variável")
                    raise Exception("Erro i< : IF não aceita valor imediato, use uma variável")
                
                if var2.isdigit():
                    print("i< var2 Erro: IF não aceita valor imediato, use uma variável")
                    raise Exception("Erro i< :: IF não aceita valor imediato, use uma variável")
                
                r1 = registradores[var1]
                r2 = registradores[var2]

                if idioma == "pt":
                    label_true = f"SE_MENOR_{label_id}"
                    label_end = f"SE_NAO_MENOR_{label_id}"

                    stack_labels.append((label_true, label_end))
                    label_id += 1

                    f.write(f"   blt t{r1}, t{r2}, {label_true}      # Se t{r1} < t{r2}, pula para {label_true}\n\n")
                    f.write(f"   j {label_end}             # Senao, pula para {label_end}\n\n")

                elif idioma == "en":
                    label_true = f"IF_LESS_{label_id}"
                    label_end = f"IF_NOT_LESS_{label_id}"

                    stack_labels.append((label_true, label_end))
                    label_id += 1

                    f.write(f"   blt t{r1}, t{r2}, {label_true}      # If t{r1} < t{r2}, jump to {label_true}\n\n")
                    f.write(f"   j {label_end}             # Otherwise jump to {label_end}\n\n")

                elif idioma == "cn":
                    label_true = f"IF_LESS_{label_id}"
                    label_end = f"IF_NOT_LESS_{label_id}"

                    stack_labels.append((label_true, label_end))
                    label_id += 1

                    f.write(f"   blt t{r1}, t{r2}, {label_true}      # 如果 t{r1} < t{r2}, 跳转到 {label_true}\n\n")
                    f.write(f"   j {label_end}             # 否则跳转到 {label_end}\n\n")

            elif linha == "IF_START":
                label_true, label_else, label_end = stack_labels[-1]
                f.write(f"{label_true}:\n")

            elif linha == "ELSE_START":
                label_true, label_else, label_end = stack_labels[-1]
                f.write(f"   j {label_end}\n")
                f.write(f"{label_else}:\n")

            elif linha == "IF_END":
                _, _, label_end = stack_labels.pop()
                f.write(f"{label_end}:\n\n")

            else:
                print("Linha não reconhecida:", linha)

# ===============================
# Executa
# ===============================
janela.mainloop()
