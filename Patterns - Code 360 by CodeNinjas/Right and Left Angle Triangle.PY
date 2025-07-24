def RightleftTriangle(n):
    
    for i in range(1, n + 1):
        # Numbers counting up (left part)
        for j in range(1, i + 1):
            print(j, end="")
        
        # Spaces
        # Calculate spaces for the current row 'i'
        current_space = 2 * (n - i)
        for _ in range(current_space): # Using '_' as a placeholder for a variable we don't need
            print(" ", end="")
            
        # Numbers counting down (right part)
        for j in range(i, 0, -1):
            print(j, end="")
            
        print() # New line after each row



# Example from the original context (assuming 'n' is passed to a function):
RightleftTriangle(4) # Let's assume n=4 for a concrete example, you can change this


# 1      1
# 12    21
# 123  321
# 12344321