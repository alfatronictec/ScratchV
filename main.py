# FAZ OPERAÇÕES BÁSICAS DA ISA RISC-V RV32I
# No momento = Soma e Subtração
# Na sequência fará BEQ   if a == b | beq rs1, rs2, label | Se rs1 == rs2, pula para o endereço indicado por label.
# Na sequência fará BLT   if a < b  | blt rs1, rs2, label | Se rs1 < rs2, o programa salta para label.
# Na sequência fará BGT   if a > b  | bgt rs1, rs2, label | Se rs1 > rs2, salta para label

import zipfile
import json
import operator
import customtkinter as ctk


OPERADORES = {
    "operator_add": operator.add,
    "operator_subtract": operator.sub,
}

OPERADOR_SIMBOLO = {
    "operator_add": "+",
    "operator_subtract": "-",
}

OPERADORES_LOGICOS = {
    "operator_gt": ">",
    "operator_lt": "<",
    "operator_equals": "="
}

COMPARADORES = {
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    "=": lambda a, b: a == b
}

controle_variaveis = []

maior = None
menor = None
igual = None

def load_sb3(path):
    with zipfile.ZipFile(path, "r") as z:
        with z.open("project.json") as f:
            return json.load(f)


# ===============================
# RESOLVER EXPRESSÕES
# ===============================

def resolver_valor(entrada, blocks, variaveis):

    tipo = entrada[0]
    valor = entrada[1]

    # literal ou variável
    if isinstance(valor, list):

        tipo_valor = valor[0]

        # número literal
        if tipo_valor == 10:
            return int(valor[1])

        # variável
        if tipo_valor == 12:
            nome = valor[1]
            return variaveis.get(nome, 0)

    # referência para outro bloco
    if isinstance(valor, str):

        bloco = blocks[valor]
        opcode = bloco["opcode"]

        if opcode in OPERADORES:

            a = resolver_valor(
                bloco["inputs"]["NUM1"],
                blocks,
                variaveis
            )

            b = resolver_valor(
                bloco["inputs"]["NUM2"],
                blocks,
                variaveis
            )

            return OPERADORES[opcode](a, b)

    return 0

def resolver_condicao(cond_id, blocks, variaveis):

    bloco = blocks[cond_id]
    opcode = bloco["opcode"]

    if opcode in OPERADORES_LOGICOS:

        entrada_a = bloco["inputs"]["OPERAND1"]
        entrada_b = bloco["inputs"]["OPERAND2"]

        # valores numéricos
        a = resolver_valor(entrada_a, blocks, variaveis)
        b = resolver_valor(entrada_b, blocks, variaveis)

        # nomes
        nome_a = extrair_nome(entrada_a, blocks)
        nome_b = extrair_nome(entrada_b, blocks)

        simbolo = OPERADORES_LOGICOS[opcode]

        return a, simbolo, b, nome_a, nome_b

    return None, None, None, None, None

def extrair_comparacao(cond_id, blocks):

    bloco = blocks[cond_id]
    opcode = bloco["opcode"]

    simbolo = OPERADOR_SIMBOLO.get(opcode, "?")

    op1 = bloco["inputs"]["OPERAND1"][1]
    op2 = bloco["inputs"]["OPERAND2"][1]

    nome1 = blocks[op1]["fields"]["VARIABLE"][0] if isinstance(op1, str) else None
    nome2 = blocks[op2]["fields"]["VARIABLE"][0] if isinstance(op2, str) else None

    return nome1, simbolo, nome2

def extrair_nome(entrada, blocks):

    valor = entrada[1]

    # literal
    if isinstance(valor, list):

        if valor[0] == 10:
            return valor[1]

        if valor[0] == 12:
            return valor[1]

    # referência para outro bloco
    if isinstance(valor, str):

        bloco = blocks[valor]

        if "fields" in bloco and "VARIABLE" in bloco["fields"]:
            return bloco["fields"]["VARIABLE"][0]

    return "?"

# ===============================
# OPCODE HANDLERS
# ===============================

def op_data_setvariableto(bloco, blocks, variaveis, codigo_python):

    variavel = bloco["fields"]["VARIABLE"][0]

    entrada = bloco["inputs"]["VALUE"]
    valor_raw = entrada[1]

    valor = resolver_valor(
        entrada,
        blocks,
        variaveis
    )

    variaveis[variavel] = valor

    # 👇 salvar no array
    controle_variaveis.append((variavel, valor))

    # detectar se vem de operador
    if isinstance(valor_raw, str):

        bloco_op = blocks[valor_raw]
        opcode_op = bloco_op["opcode"]

        if opcode_op in OPERADORES:

            simbolo = OPERADOR_SIMBOLO[opcode_op]

            linha_python = f"vr{simbolo}={variavel}"

        else:
            linha_python = f"v={variavel} = {valor}"

    else:
        linha_python = f"v={variavel} = {valor}"

    codigo_python.append(linha_python)


def op_data_showvariable(bloco, blocks, variaveis, codigo_python):

    variavel = bloco["fields"]["VARIABLE"][0]

    linha_python = f"p={variavel}"

    codigo_python.append(linha_python)


def op_control_if(bloco, blocks, variaveis, codigo_python):

    cond_id = bloco["inputs"]["CONDITION"][1]

    a, op, b, nome_a, nome_b = resolver_condicao(cond_id, blocks, variaveis)

    codigo_python.append(f"i{op}={nome_a}|{nome_b}")
    codigo_python.append("IF_START")

    stack = bloco["inputs"]["SUBSTACK"][1]

    while stack:

        b_stack = blocks[stack]
        opcode = b_stack["opcode"]

        if opcode in OPCODE_HANDLERS:
            OPCODE_HANDLERS[opcode](
                b_stack,
                blocks,
                variaveis,
                codigo_python
            )

        stack = b_stack["next"]

    codigo_python.append("IF_END")

OPCODE_HANDLERS = {
    "data_setvariableto": op_data_setvariableto,
    "data_showvariable": op_data_showvariable,
    "control_if": op_control_if
}

# ===============================
# CARREGAR PROJETO
# ===============================

project = load_sb3("teste_igual_BEQ.sb3")

codigo_python = []

for target in project["targets"]:

    #print("\n==== TARGET ====")
    #print("Name:", target["name"])
    #print("Is stage:", target["isStage"])

    blocks = target["blocks"]

    for block_id, block in blocks.items():

        if block["topLevel"]:

            #print("\n--- SCRIPT START ---")
            #print("Start block:", block["opcode"])

            ordered_blocks = []
            current = block_id

            while current is not None:
                b = blocks[current]
                ordered_blocks.append((current, b))
                current = b["next"]

            #print("\nLISTA DE BLOCOS EM ORDEM:\n")

            linhas = []
            variaveis = {}

            for i, (bid, b) in enumerate(ordered_blocks, start=1):

                print(f"BLOCO {i}")
                print("id:", bid)
                print("opcode:", b["opcode"])
                print("next:", b["next"])
                print("parent:", b["parent"])
                print("inputs:", b["inputs"])
                print("fields:", b["fields"])
                print("topLevel:", b["topLevel"])
                print()

                linha = (
                    f"{i}:id:|{bid}|"
                    f"opcode:|{b['opcode']}|"
                    f"next:|{b['next']}|"
                    f"parent:|{b['parent']}|"
                    f"inputs:|{b['inputs']}|"
                    f"fields:|{b['fields']}|"
                    f"topLevel:|{b['topLevel']}|"
                )

                linhas.append(linha)

                # ===============================
                # TRADUTOR SCRATCH -> PYTHON
                # ===============================

                opcode = b["opcode"]

                if opcode in OPCODE_HANDLERS:
                    OPCODE_HANDLERS[opcode](
                        b,
                        blocks,
                        variaveis,
                        codigo_python
                    )

            # separar campos das linhas

            blocos = []

            for linha in linhas:

                partes = linha.split("|")

                bloco = [
                    partes[1],   # id
                    partes[3],   # opcode
                    partes[5],   # next
                    partes[7],   # parent
                    partes[9],   # inputs
                    partes[11],  # fields
                    partes[13]   # topLevel
                ]

                blocos.append(bloco)


print("NUMERO DE BLOCOS:")
print(len(linhas))


print("\nCODIGO PYTHON GERADO:\n")

for linha in codigo_python:
    print(linha)

reg = 0
ultimo_reg = None
registradores = {}
label_id = 0
stack_labels = []

with open("codigo_gerado.asm", "w", encoding="utf-8") as f:

    f.write(".text\n\n")

    for linha in codigo_python:

        # =========================
        # ATRIBUIÇÃO
        # =========================
        if linha.startswith("v="):

            partes = linha.split("=")

            var = partes[1].strip()

            # valor literal
            if len(partes) > 2 and partes[2].strip().isdigit():

                valor = partes[2].strip()

                f.write(f"   li t{reg}, {valor}     # Armazena o valor {valor} no registrador t{reg}\n\n")

                registradores[var] = reg
                ultimo_reg = reg
                reg += 1

            else:
                # recebe resultado da operação anterior
                registradores[var] = ultimo_reg

                f.write(f"   # {var} -> t{ultimo_reg}\n\n")


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