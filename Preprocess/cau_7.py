import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 3:
        print("To run: `python cau_7.py norminalize method`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #7
    if (function == 'norminalize'):
        print('---------Norminalize---------')
        if len(sys.argv) < 3:
            print("To run: `python cau_7.py norminalize method`")
            print("WARMING: Must be provided enough argument!\n")

        method = sys.argv[2]
        op.norminalize(data,method)
