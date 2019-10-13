##What is Recursion
    - a method (procedure) where a solution to a problem depens 
      on solution to smaller instances of the same problem.
    - we break a tast into the smaller subtasks.
    - the approach can be apply to many type of prtoblems, 
      and recusrion is on of the central idea of comouter science.
    - we have to define the base case in order to avoid infinite loops.
    - we can solve the problems with recursion or with iteration
       >> we can transform recusion to iteration and vice versa.
       
 
 ### Head and Tail
 #### Head recursion:
    - if the recusion call occurs at he beginning of the function then 
      it is called a head recusion;
      >> the method saves the state before jumping into the next recursive call.
      >> which means that head recusion needs more memory
         because we have to store the states of the actual function calls.
 #### Tail recursion:
    - if the recursion call at the end of the function the it is call tail recursion.
      >> the tail recursion is similar to a loop(for or while loop)
      >> this method executes all the statements before jumping to the next recursive call.
 