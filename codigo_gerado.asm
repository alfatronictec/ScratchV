.text

   li t0, 2                 # Store the value 2 in register t0

   li t1, 5                 # Store the value 5 in register t1

   li t2, 6                 # Store the value 6 in register t2

   li t3, 0                 # Store the value 0 in register t3

   li t4, 0                 # Store the value 0 in register t4

   add t5, t0, t1              # Soma o valor armazenado em t0 com o armazenado em t1 e armazena o resultado no registrador t5 

   bgt t5, t2, IF_GREATER_0      # If t5 > t2, jump to IF_GREATER_0

   j IF_END_0             # Otherwise jump to IF_END_0

IF_GREATER_0:
   li t3, 7                 # Store the value 7 in register t3

