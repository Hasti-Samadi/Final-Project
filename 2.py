import numpy as np
import os

def electric_field(grid):
    n, m = grid.shape
    ex, ey = np.zeros((n, m)), np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if grid[i, j] != 0:
                for x in range(n):
                    for y in range(m):
                        if (x, y) != (i, j):
                            dx, dy = x - i, y - j
                            r_squared = dx**2 + dy**2
                            ex[x, y] += grid[i, j] * dx / r_squared
                            ey[x, y] += grid[i, j] * dy / r_squared
    return ex, ey

def electric_field_line(charge_density, length, point):
    k = 8.99e9  # N·m²/C² (constant)
    ex, ey = 0, 0
    for x in range(length):
        dx = point[0] - x
        r = np.sqrt(dx**2)
        ex += (k * charge_density) / r
    return ex, ey

# Read input from a file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        grid = []
        for line in lines:
            row = []
            for char in line.strip().split():
                try:
                    row.append(int(char))
                except ValueError:
                    # Replace invalid characters with 0
                    row.append(0)
            grid.append(row)
        return np.array(grid)

# Write output to a file
def write_output(file_name, ex, ey):
    with open(file_name, 'w') as file:
        file.write("Electric field (x):\n")
        file.write(np.array2string(ex) + '\n')
        file.write("Electric field (y):\n")
        file.write(np.array2string(ey) + '\n')

# Input file name
current_directory = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_directory, 'input.txt')
input_file = input_path
# Output file name
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, 'output.txt')
output_file = output_path

# Read grid from input file
grid = read_input(input_file)

# Calculate electric field
ex, ey = electric_field(grid)

# Write results to output file
write_output(output_file, ex, ey)
