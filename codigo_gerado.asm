.text

   li t0, 3                 # Store the value 3 in register t0

   li t1, 5                 # Store the value 5 in register t1

   add t2, t0, t1   # Add the value stored in t1 to the value stored in t0 and store the result in the register t2 

   li a7, 1             # Loads the value 1 into register a7, which defines the syscall code (system service); 1 = print integer  
   add a0, t2, zero    # Copies the value from register t2 to a0; a0 is the register used to pass the syscall argument, the integer that will be printed   
   ecall                # Performs an environment call

