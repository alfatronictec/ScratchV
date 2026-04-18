# ScratchV

## Idiomas

- 🇺🇸 [English](README.md)
- 🇧🇷 [Português (Brasil)](README.pt-br.md)
- 🇪🇸 [Español](README.es.md)
  
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

  - se menor que 

- Geração de código compatível com simuladores RISC-V, como:  

  - RARS  

  - RIPES 

  - Entre outros
 
## Como usar

O ScratchV converte programas criados no Scratch (.sb3) em código assembly RISC-V (.asm).

Siga os passos abaixo para utilizar a ferramenta.

<br><br>
Passo 1 — Criar o programa no Scratch.
<br><br>

-  Inicie o código com o seguinte bloco: Quando For Clicado

  ![When Clicked](images/images%20readme/when_clicked.png)

- Finalize o código com o seguinte bloco: Pare Todos

  ![When Clicked](images/images%20readme/stop%20all.png)

- No seu código no Scratch, utilize apenas as seguintes operações:
  
  - Adição e Subtração:

    ![When Clicked](images/images%20readme/operations.png)

  - Operadores Condicionais: se igual, se maior e se menor:

    ![When Clicked](images/images%20readme/conditions.png)

Segue abaixo um exemplo de codigo:

![When Clicked](images/images%20readme/image%20example.png)

<br><br>
Passo 2 — Baixar o arquivo .sb3.
<br><br>

Após criar o programa no Scratch:

1- Clique em Arquivo <br>
2- Clique em Baixar para seu computador <br>
3- O Scratch irá gerar um arquivo .sb3 <br>
4- Verifique onde o arquivo foi salvo no seu computador <br>

<br><br>
Step 3 — Carregar o arquivo .sb3 no ScratchV.
<br><br>

1- Abra o ScratchV e selecione seu idioma na bandeira no canto superior direito.
2- Carregue o arquivo .sb3 <br>
3- Após carregar o arquivo, o ScratchV irá gerar o arquivo .asm no seu computador <br>
