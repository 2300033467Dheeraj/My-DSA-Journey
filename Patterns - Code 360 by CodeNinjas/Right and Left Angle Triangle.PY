def generate_pattern(rows):
    for i in range(1, rows + 1):
        # Left side: numbers counting up
        left_side = ""
        for j in range(1, i + 1):
            left_side += str(j)
        
        # Right side: numbers counting down
        right_side = ""
        for j in range(i, 0, -1):
            right_side += str(j)
        
        print(f"{left_side}\t{right_side}")

# Example usage for 5 rows, matching your image:
generate_pattern(5)