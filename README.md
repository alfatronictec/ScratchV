# ScratchV

## Download

[⬇️ Download ScratchV (.exe)](https://github.com/alfatronictec/ScratchV/releases/download/v1.0/ScratchV.exe)

## Requirements

- Windows 10/11
  
## Languages

- 🇺🇸 [English](README.md)
- 🇧🇷 [Português (Brasil)](README.pt-br.md)
- 🇪🇸 [Español](README.es.md)

ScratchV is an educational tool that translates programs developed in Scratch into RISC-V assembly, allowing students to understand the relationship between block-based programming and low-level programming.

The goal of the project is to facilitate the teaching of computer architecture, computer organization, and assembly languages by connecting visual programming with execution on RISC-V architecture. 

![Tela Inicial](images/images%20readme/interface.png)

## Motivation 

Environments like Scratch are widely used in introductory programming education. However, there is a significant gap between block-based programming and the inner workings of low-level languages, such as Assembly. 

ScratchV was developed to bridge this gap, allowing students to use programs created in Scratch (.sb3) and observe their conversion to RISC-V Assembly. 

As a result, ScratchV aids in the learning of concepts such as: 

program execution flow  

low-level arithmetic operations  

conditional structures  

basic functioning of the RISC-V architecture  

The tool’s purpose is to support introductory Assembly instruction using a high-level visual language, such as Scratch. 

## Features 

ScratchV currently allows: 

- Loading of .sb3 files generated in Scratch  

- Automatic conversion to RISC-V assembly code (.asm)  

- Support for basic arithmetic operations:  

  - addition  

  - subtraction  

- Support for conditional structures:  

  - if equal  

  - if greater than  

  - if less than  

- Generation of code compatible with RISC-V simulators, such as:  

  - RARS  

  - RIPES 

  - Other RISC-V simulators
 
## How to Use 

ScratchV converts programs created in Scratch (.sb3) into RISC-V assembly code (.asm). 

Follow the steps below to use the tool. 

### Step 1 — Create the program in Scratch

-  Start the code with the following block:

  ![When Clicked](images/images%20readme/when_clicked.png)

- End the code with the following block:

  ![When Clicked](images/images%20readme/stop%20all.png)

- In your Scratch code, use only the following operations:
  
  - Addition and subtraction:

    ![When Clicked](images/images%20readme/operations.png)

  - Conditional operators: if equal, if greater than, and if less than:

    ![When Clicked](images/images%20readme/conditions.png)

Here is an example of the code:

![When Clicked](images/images%20readme/image%20example.png)

### Step 2 — Export the .sb3 file

After creating the program in Scratch: 

1- Click File <br>
2- Click Save to your computer <br>
3- Scratch will generate an .sb3 file <br>
4- Check where the file was saved on your computer <br>

### Step 3 — Load the .sb3 file into ScratchV

1- Run ScratchV, Select your language from the flags in the upper-right corner.
2- Load the .sb3 file <br>
2- After loading the file, ScratchV will generate the .asm file on your computer <br>
