import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 3:
        print("To run: `python cau_4.py remove_empty_rows threshold`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #4
    if (function == 'remove_empty_rows'):
        print('---------Remove empty rows---------')
        if len(sys.argv) < 3:
            print("To run: `python cau_4.py remove_empty_rows threshold`")
            print("WARMING: Must be provided enough argument!\n")

        threshold = sys.argv[2]
        op.remove_empty_rows_with_threshold(data, threshold)
