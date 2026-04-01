.text

   li t0, 5                 # Armazena o valor 5 no registrador t0

   li t1, 2                 # Armazena o valor 2 no registrador t1

   sub t2, t0, t1   # var_final = var_1 - var_2

   li a7, 1             # Carrega o valor 1 no registrador a7, que define o codigo da syscall (servico do sistema), 1 = imprimir inteiro (print integer) 
   add a0, t2, zero    # Copia o valor do registrador t2 para a0, a0 é o registrador usado para passar o argumento da syscall, o inteiro que será impresso  
   ecall                # Executa uma chamada de sistema (environment call)

