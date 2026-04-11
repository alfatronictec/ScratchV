.text

   li t0, 5                 # Armazena o valor 5 no registrador t1

   li t1, 5                 # Armazena o valor 5 no registrador t2

   li t2, 0                 # Armazena o valor 0 no registrador t3

   beq t0, t1, SE_IGUAL_0      # Se var_1 == var_2, pula para SE_IGUAL_0
   j FIM_SE_0                       # Caso contrário, pula para FIM_SE_0

