import numpy as np

def example_homogenous_types():
    # Read in the data
    data = np.genfromtxt(
        'toy-homogenous-types.csv', # filename
        delimiter=',', # csv cells are demarcated with commas
        names=None, # There is no header information in the first row
        dtype=np.float32 # This informs how all data should be interpreted
    )

    print('Homogenous data example:\n')
    print(f'\tData:\n{data}') # this is a normal numpy array of floats
    print(f'\tData type(s):\n{data.dtype}')
    print(f'\tIndexing row 0 column 1:\n{data[0,1]}') # first index is row, second index is column
    print(f'\tSumming over column 2:\n{data[:,2].sum()}')
    print(f'\tWhich rows are less than 0.6 in the first column?\n{data[:,0] < 0.6}')
    print(f'\tWhat are the rows with less than 0.6 in the first column?\n{data[data[:,0] < 0.6]}')

def example_heterogenous_types():
    '''
    Data is not normally stored with heterogenous types in numpy, so you can concieve of each column as its own array, indexed by column name
    '''

    # Specify ahead of time the different column types to use
    column_types = (
        np.float32, # allows storing fractional parts of age (e.g. 34.5)
        np.dtype('U5'), # no string exceeds 6 characters
        np.dtype('U1'), # no string exceeds 1 character
        np.uint8, # unsigned 8 bit integer (can store values between 0 and 255 inclusive)
    )

    # Read in the data
    data = np.genfromtxt(
        'toy-heterogenous-types.csv', # filename
        delimiter=',', # csv cells are demarcated with commas
        names=True, # The first row is the column names. Using `names=True` prevents it from being treated as data, and instead makes the array indexable by them
        dtype=column_types # This informs how each column should be interpreted
    )

    print('Heterogenous data example:\n')
    print(f'\tData:\n{data}')
    print(f'\tData type(s):\n{data.dtype}')

    # Notice that if we index by number, we get a row (like normal), but if we index by string, we get a column
    print(f'\tIndexing row 0:\n{data[0]}')
    print(f'\tIndexing by column name "Player_Name", and row 0:\n{data["Player_Name"][0]}') # Notice that we indexed by column FIRST, and then we treated the result as a normal array of homogenous type to be numerically indexed
    print(f'\tSumming over "High_Score" column:\n{data["High_Score"].sum()}')

def main():
    print()
    example_homogenous_types()
    print('\n\n')
    example_heterogenous_types()

if __name__ == '__main__':
    main()
