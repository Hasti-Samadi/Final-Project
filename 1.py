import numpy as np
import os

def convolution(signal, filter):
    n = len(signal)
    m = len(filter)
    output = np.zeros(n + m - 1)
    for i in range(n):
        for j in range(m):
            output[i + j] += signal[i] * filter[j]
    return output

def low_pass_filter(signal, cutoff):
    return [s if s < cutoff else 0 for s in signal]

def high_pass_filter(signal, cutoff):
    return [s if s > cutoff else 0 for s in signal]

def main(input_file, output_snape, output_griffindor):
    # خواندن سیگنال از فایل ورودی
    with open(input_file, 'r') as f:
        signal = np.array([float(x) for x in f.readline().split()])

    low_cutoff = 0.02 * np.pi
    high_cutoff = 0.2 * np.pi

    # اعمال فیلترها
    signal_snape = high_pass_filter(signal, high_cutoff)
    signal_griffindor = low_pass_filter(signal, low_cutoff)

    # نوشتن سیگنال‌های دفتر اسنیپ و گریفندور به فایل‌های خروجی
    with open(output_snape, 'w') as f:
        f.write("Signal Snape: " + ' '.join(map(str, signal_snape)) + '\n')

    with open(output_griffindor, 'w') as f:
        f.write("Signal Griffindor: " + ' '.join(map(str, signal_griffindor)) + '\n')

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_directory, 'input.txt')
    input_file = input_path
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path1 = os.path.join(current_directory, "output_snape.txt")
    output_snape = output_path1
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path2 = os.path.join(current_directory, "output_griffindor.txt")
    output_griffindor = output_path2
    main(input_file, output_snape, output_griffindor)
