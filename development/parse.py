#   import numpy as np
#   import pandas as pd
#   import matplotlib.pyplot as plt
#   import seaborn as sns

# Get number of rows and columns in input file
def get_dims(address):
    with open(address, 'r') as file:
        rows = 0
        cols = 1
        first_line = 1
        for line in file:
            if first_line:
                for char in line:
                    if char == ';':
                        cols += 1
                        first_line = 0
            rows += 1
    print('\nRows: ' + str(rows) + '\nColumns: ' + str(cols))
    return [rows, cols]


# Create matrix of zeros with size matching input file
def get_data(address, rows, cols):
    with open(address, 'r') as file:
        print('\nParsing data from ' + address + '...')
        data = [x[:] for x in [[''] * cols] * rows]

        # Fill matrix data from input file
        file.seek(0)
        r = 0
        for line in file:
            c = 0
            for char in line:
                if (char != ';') and (char != '\n'):
                    data[r][c] += char
                else:
                    c += 1
            r += 1


    # Print matrix preview
    print('\nData Preview:')
    # print('Upper-left corner:')
    for i in range(0, 5):
        for j in range(0, 5):
            print('[' + str(data[i][j]) + "] ", end='')
        print('...')
    print('...')
    # print('Bottom-right corner:')
    # print('...')
    # for i in range(ROWS-5, ROWS):
    #     print('...')
    #     for j in range(COLS-5, COLS):
    #         print('[' + str(data[i][j]) + "] ", end='')


