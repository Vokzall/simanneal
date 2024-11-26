
import os
import random
import time
from math import exp

def tcf_funct(byte, T):
    # your function implementation here
    pass

def invert_bits(byte):
    mask = random.getrandbits(8)
    return byte ^ mask

def parse_input(file):
    n = None
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('power:'):
                n = int(line.split(':')[1])
                break
    return n

def main():
    Tmin = 0.1
    T = 10
    Tstep = 0.1
    P = 0.0

    filename = 'output.txt'
    input_filename = 'input.txt'

    byte = random.getrandbits(8)
    with open(filename, 'w') as f:
        f.write(byte.to_bytes(1, byteorder='big').hex())

    old_data = os.stat(input_filename).st_mtime

    while T > Tmin:
        if os.stat(input_filename).st_mtime != old_data:
            n_new = parse_input(input_filename)
            n_old = tcf_funct(byte, T)
            if n_new > n_old:
                tcf_funct(byte, T, n_new)
            else:
                P = exp((n_old - n_new) / T)
                if random.random() < P:
                    tcf_funct(byte, T, n_new)

            old_data = os.stat(input_filename).st_mtime

        byte = invert_bits(byte)
        with open(filename, 'w') as f:
            f.write(byte.to_bytes(1, byteorder='big').hex())

        time.sleep(1)
        T -= Tstep

if __name__ == '__main__':
    main()
