import os
def calculate_turns(V_primary, V_secondary, N_primary):
    N_secondary = (V_secondary / V_primary) * N_primary
    return N_primary, N_secondary

def calculate_core_area(P, B_max, f):
    A_core = P / (4.44 * B_max * f)
    return A_core

# Read input from a file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # Assuming input file contains each parameter on a separate line
        V_primary = float(lines[0].strip())
        V_secondary = float(lines[1].strip())
        N_primary = int(lines[2].strip())
        P = float(lines[3].strip())
        B_max = float(lines[4].strip())
        f = float(lines[5].strip())
        return V_primary, V_secondary, N_primary, P, B_max, f

# Write output to a file
def write_output(file_name, N_primary, N_secondary, A_core):
    with open(file_name, 'w') as file:
        file.write("Primary Turns: {}\n".format(N_primary))
        file.write("Secondary Turns: {}\n".format(N_secondary))
        file.write("Core Area: {}\n".format(A_core))

# Input file name
current_directory = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_directory, "input.txt")
input_file = input_path
# Output file name
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory, "output.txt")
output_file = output_path

# Read input parameters from input file
V_primary, V_secondary, N_primary, P, B_max, f = read_input(input_file)

# Calculate turns and core area
N_primary, N_secondary = calculate_turns(V_primary, V_secondary, N_primary)
A_core = calculate_core_area(P, B_max, f)

# Write results to output file
write_output(output_file, N_primary, N_secondary, A_core)
