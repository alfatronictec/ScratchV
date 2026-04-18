# ScratchV

Idiomas

- 🇺🇸 English → [README](README.md)
- 🇧🇷 Português (Brasil) → [README.pt-br.md](README.pt-br.md)
- 🇪🇸 Español → [README.es.md](README.es.md)
  
ScratchV é uma ferramenta educacional que traduz programas desenvolvidos no Scratch para assembly RISC-V, permitindo que os estudantes entendam a relação entre programação baseada em blocos e programação de baixo nível.

O objetivo do projeto é facilitar o ensino de arquitetura de computadores, organização de computadores e linguagens de assembly, conectando a programação visual com a execução na arquitetura RISC-V.

![Tela Inicial](images/images%20readme/interface.png)

## Motivação

Ambientes como o Scratch são amplamente utilizados no ensino introdutório de programação. No entanto, existe uma lacuna significativa entre a programação baseada em blocos e o funcionamento interno de linguagens de baixo nível, como Assembly.

O ScratchV foi desenvolvido para preencher essa lacuna, permitindo que estudantes utilizem programas criados no Scratch (.sb3) e observem sua conversão para Assembly RISC-V.

Como resultado, o ScratchV auxilia no aprendizado de conceitos como:

- Fluxo de execução de programas
- Operações aritméticas de baixo nível
- Estruturas condicionais
- Funcionamento básico da arquitetura RISC-V

O objetivo da ferramenta é apoiar o ensino introdutório de Assembly utilizando uma linguagem visual de alto nível, como o Scratch.

## Funcionalidades

O ScratchV atualmente permite:

- Carregamento de arquivos .sb3 gerados no Scratch

- Conversão automática para código assembly RISC-V (.asm) 

- Suporte a operações aritméticas básicas:  

  - adição 

  - subtração

- Suporte a estruturas condicionais:  

  - se igual 

  - se maior que 

  - if menor que 

- Geração de código compatível com simuladores RISC-V, como:  

  - RARS  

  - RIPES 

  - Entre outros
 
## Como usar

ScratchV converts programs created in Scratch (.sb3) into RISC-V assembly code (.asm). 

Follow the steps below to use the tool. 

<br><br>
Step 1 — Create the program in Scratch.
<br><br>

-  Start the code with the following block:

  ![When Clicked](images/images%20readme/when_clicked.png)

- End the code with the following block:

  ![When Clicked](images/images%20readme/stop%20all.png)

- In your Scratch code, use only the following operations:
  
  - Addition and subtraction:

    ![When Clicked](images/images%20readme/operations.png)

  - Conditional operators: if equal, if greater than, and if equal:

    ![When Clicked](images/images%20readme/conditions.png)

Here is an example of the code:

![When Clicked](images/images%20readme/image%20example.png)

<br><br>
Step 2 — Export the .sb3 file.
<br><br>

After creating the program in Scratch: 

1- Click File <br>
2- Click Save to your computer <br>
3- Scratch will generate an .sb3 file <br>
4- Check where the file was saved on your computer <br>

<br><br>
Step 3 — Load the .sb3 file into ScratchV.
<br><br>

1- Run ScratchV and load the .sb3 file <br>
2- After loading the file, ScratchV will generate the .asm file on your computer <br>
