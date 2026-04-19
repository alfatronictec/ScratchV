.text

   li t0, 5                 # Almacena el valor 5 en el registro t0

   li t1, 5                 # Almacena el valor 5 en el registro t1

   li t2, 0                 # Almacena el valor 0 en el registro t2

   beq t0, t1, IF_EQUAL_0      # Compara los valores almacenados; si t0 = t1, salta a IF_EQUAL_0; si no, continúa 
   j IF_END_0             # Saltar a IF_END_0 si es diferente 

IF_EQUAL_0:
   li t2, 5                 # Almacena el valor 5 en el registro t2

IF_END_0:

   li a7, 1             # Carga el valor 1 en el registro a7, que define el código de la llamada al sistema (syscall), 1 = imprimir entero (print integer) 
   add a0, t2, zero    # Copia el valor del registro t2 a a0; a0 es el registro que se utiliza para pasar el argumento de la llamada al sistema, el entero que se imprimirá  
   ecall                # Ejecuta una llamada al sistema (environment call)

