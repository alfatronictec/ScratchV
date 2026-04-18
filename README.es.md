# ScratchV

Idiomas

- 🇺🇸 English → [README](README.md)
- 🇧🇷 Português (Brasil) → [README.pt-br.md](README.pt-br.md)
- 🇪🇸 Español → [README.es.md](README.es.md)
  
ScratchV es una herramienta educativa que traduce programas desarrollados en Scratch a ensamblador RISC-V, lo que permite a los estudiantes comprender la relación entre la programación basada en bloques y la programación de bajo nivel.

El objetivo del proyecto es facilitar la enseñanza de la arquitectura de ordenadores, la organización de los ordenadores y los lenguajes de ensamblador, vinculando la programación visual con la ejecución en la arquitectura RISC-V.

![Tela Inicial](images/images%20readme/interface.png)

## Motivación

Entornos como Scratch se utilizan ampliamente en la enseñanza introductoria de la programación. Sin embargo, existe una brecha significativa entre la programación basada en bloques y el funcionamiento interno de los lenguajes de bajo nivel, como el ensamblador.

ScratchV se ha desarrollado para cubrir esta brecha, permitiendo a los estudiantes utilizar programas creados en Scratch (.sb3) y observar su conversión a ensamblador RISC-V.

Como resultado, ScratchV ayuda a aprender conceptos como:

- Flujo de ejecución de programas
- Operaciones aritméticas de bajo nivel
- Estructuras condicionales
- Funcionamiento básico de la arquitectura RISC-V

## Funcionalidades

Actualmente, ScratchV permite:

- Cargar archivos .sb3 generados en Scratch

- Conversión automática a código ensamblador RISC-V (.asm) 

- Compatibilidad con operaciones aritméticas básicas:  

  - suma 

  - resta

- Compatibilidad con estructuras condicionales:  

  - si es igual 

  - si es mayor que 

  - si es menor que 

- Generación de código compatible con simuladores RISC-V, como:  

  - RARS  

  - RIPES 

  - Entre otros
 
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

1- Abra o ScratchV e carregue o arquivo .sb3 <br>
2- Após carregar o arquivo, o ScratchV irá gerar o arquivo .asm no seu computador <br>
