import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 2:
        print("To run: `python cau_3.py fill_empty_value attribute method`")
        print("OR")
        print("To run: `python cau_3.py fill_empty_value`")
        print("WARMING: Must be provided appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #3
    if (function == 'Fill empty value'):
        print('---------Fill empty value---------')
        if len(sys.argv) == 4:          
            attribute = sys.argv[2]
            method = sys.argv[3]
            op.fill_empty_value(data,attribute,method)
        elif len(sys.argv) == 2:
            op.fill_empty_value(data)
        else:
            print("To run: `python main.py fill_empty_value attribute method`")
            print("OR")
            print("To run: `python main.py fill_empty_value`")
            print("WARMING: Must be provided appropriate argument!\n")
