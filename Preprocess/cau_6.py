import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 2:
        print("To run: `python cau_6.py remove_duplicate`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #6
    if (function == 'remove_duplicate'):
        print('---------Remove_duplicate---------')
        op.removeDuplicate(data)
