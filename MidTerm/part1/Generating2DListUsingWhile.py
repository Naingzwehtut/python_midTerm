#15
rows = 3  
cols = 4  
matrix = []  
i = 0  
while i < rows:  
    row = []  
    j = 0  
    while j < cols:  
        row.append(i * j)  
        j += 1  
    matrix.append(row)  # Add the row to the matrix
    i += 1  # Increment the outer loop counter
    
print("Generated Matrix:")  # Blank 5: Print the matrix header
for row in matrix:
    print(row) # Print each row of the matrix
