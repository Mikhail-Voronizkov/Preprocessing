import csv
import operation as op


if __name__ == '__main__':
    """
        Argument from command line. To run: `python main.py function arg1 arg2 ..`
    """
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 2:
        print("To run: `python cau_1.py count_missing_row`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #2
    if (function == 'count_missing_row'):
        print('---------Count missing row---------')
        f = op.count_missing_row(data)
        print('Total rows in dataset: ', f[0], ' missing rows: ', f[1])
