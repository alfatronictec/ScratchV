.text

   li t0, 3     # Armazena o valor 3 no registrador t0

   li t1, 5     # Armazena o valor 5 no registrador t1

   add t2, t0, t1   # Soma o valor armazenado em t1 com o armazenado em t0 e armazena no registrador t2 

   li a7, 1
   add a0, t2, zero
   ecall

