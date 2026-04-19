# ScratchV

## Descargar

[⬇️ Descargar ScratchV (.exe)](https://github.com/alfatronictec/ScratchV/releases/download/v1.0/ScratchV.exe)

## Requisitos

- Windows 10/11

## Idiomas

- 🇺🇸 [English](README.md)
- 🇧🇷 [Português (Brasil)](README.pt-br.md)
- 🇪🇸 [Español](README.es.md)
  
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
 
## Cómo utilizarlo

ScratchV convierte los programas creados en Scratch (.sb3) en código ensamblador RISC-V (.asm).

Sigue los pasos que se indican a continuación para utilizar la herramienta.

<br><br>
Paso 1 — Crea el programa en Scratch.
<br><br>

-  Comience el código con el siguiente bloque: Al hacer clic en

  ![When Clicked](images/images%20readme/when_clicked.png)

- Finalice el código con el siguiente bloque: Detener todos

  ![When Clicked](images/images%20readme/stop%20all.png)

- En tu código de Scratch, utiliza únicamente las siguientes operaciones:
  
  - Suma y resta:

    ![When Clicked](images/images%20readme/operations.png)

  - Operadores condicionales: si es igual, si es mayor y si es menor:

    ![When Clicked](images/images%20readme/conditions.png)

A continuación se muestra un ejemplo de código:

![When Clicked](images/images%20readme/image%20example.png)

<br><br>
Paso 2 — Descargar el archivo .sb3.
<br><br>

Después de crear el programa en Scratch:

1- Haz clic en Archivo <br>
2- Haz clic en Guardar en tu ordenador <br>
3- Scratch generará un archivo .sb3 <br>
4- Comprueba dónde se ha guardado el archivo en tu ordenador <br>

<br><br>
Paso 3 — Cargar el archivo .sb3 en ScratchV.
<br><br>

1- Abre ScratchV y selecciona tu idioma en las banderas de la esquina superior derecha
2- Carga el archivo .sb3 <br>
3- Tras cargar el archivo, ScratchV generará el archivo .asm en tu ordenador <br>
