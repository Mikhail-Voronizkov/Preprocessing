import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 3:
        print("To run: `python cau_5.py remove_empty_cols threshold`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #5
    if (function == 'remove_empty_cols'):
        print('---------Remove empty columns---------')
        if len(sys.argv) < 3:
            print("To run: `python cau_5.py remove_empty_cols threshold`")
            print("WARMING: Must be provided enough argument!\n")

        threshold = sys.argv[2]
        op.remove_empty_cols_with_threshold(data, threshold)
