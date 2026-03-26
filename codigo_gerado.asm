.text

   li t0, 5     # Armazena o valor 5 no registrador t0

   li t1, 5     # Armazena o valor 5 no registrador t1

   beq t0, t1, IF_TRUE_0
   j IF_END_0

IF_TRUE_0:
   li t2, 5     # Armazena o valor 5 no registrador t2

IF_END_0:

   li a7, 1
   add a0, t2, zero
   ecall

