# FAZ OPERAÇÕES BÁSICAS DA ISA RISC-V RV32I
# No momento = Soma e Subtração
# Na sequência fará BEQ   if a == b | beq rs1, rs2, label | Se rs1 == rs2, pula para o endereço indicado por label.
# Na sequência fará BLT   if a < b  | blt rs1, rs2, label | Se rs1 < rs2, o programa salta para label.
# Na sequência fará BGT   if a > b  | bgt rs1, rs2, label | Se rs1 > rs2, salta para label

from core import load_sb3, gerar_codigo_python

project = load_sb3("teste_add.sb3")

codigo_python = gerar_codigo_python(project)

print("\nCODIGO GERADO:\n")
for linha in codigo_python:
    print(linha)

def gerar_assembly(codigo_python):

    reg = 0
    ultimo_reg = None
    registradores = {}
    label_id = 0
    stack_labels = []

    with open("codigo_gerado.asm", "w") as f:

        f.write(".text\n\n")

        for linha in codigo_python:

            if linha.startswith("v="):
                partes = linha.split("=")
                var = partes[1].strip()

                if len(partes) > 2 and partes[2].strip().isdigit():
                    valor = partes[2].strip()

                    f.write(f"   li t{reg}, {valor}     # Armazena o valor {valor} no registrador t{reg}\n\n")

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

                f.write(f"   add t{reg}, t{reg-2}, t{reg-1}   # Soma o valor armazenado em t{reg-1} com o armazenado em t{reg-2} e armazena no registrador t{reg} \n\n")

                registradores[var] = reg  

                ultimo_reg = reg
                reg += 1

            # =========================
            # SUBTRAÇÃO
            # =========================
            elif linha.startswith("vr-"):

                var = linha.split("=")[1].strip()

                f.write(f"   sub t{reg}, t{reg-2}, t{reg-1}   # Subtrai o valor armazenado em t{reg-1} do valor armazenado em t{reg-2} e armazena no registrador t{reg} \n\n")

                registradores[var] = reg  
                ultimo_reg = reg
                reg += 1

            # =========================
            # PRINT
            # =========================
            elif linha.startswith("p="):

                var = linha.split("=")[1].strip()
                r = registradores[var]

                f.write("   li a7, 1\n")
                f.write(f"   add a0, t{r}, zero\n")
                f.write("   ecall\n\n")


            # =========================
            # IF IGUAL (BEQ)
            # =========================
            elif linha.startswith("i="):

                conteudo = linha[3:]
                var1, var2 = conteudo.split("|")

                r1 = registradores[var1]
                r2 = registradores[var2]

                label_true = f"IF_TRUE_{label_id}"
                label_end = f"IF_END_{label_id}"

                stack_labels.append((label_true, label_end))
                label_id += 1

                f.write(f"   beq t{r1}, t{r2}, {label_true}\n")
                f.write(f"   j {label_end}\n\n")
            
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


gerar_assembly(codigo_python)