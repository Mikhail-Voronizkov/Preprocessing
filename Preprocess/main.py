import csv
import operation as op


if __name__ == '__main__':
    """
        Argument from command line. To run: `python main.py function arg1 arg2 ..`
    """
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 2:
        print("To run: `python main.py function arg1 arg2 ..`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]
    #1
    if (function == 'missing_attribute'):
        print('---------Missing attribute---------')
        print(op.missing_data_attribute(data))
    #2
    elif (function == 'count_missing_row'):
        print('---------Count missing row---------')
        f = op.count_missing_row(data)
        print('Total rows in dataset: ', f[0], ' missing rows: ', f[1])
    #3
    elif (function == 'Fill empty value'):
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
    #4
    elif (function == 'remove_empty_rows'):
        print('---------Remove empty rows---------')
        if len(sys.argv) < 3:
            print("To run: `python main.py remove_empty_rows threshold`")
            print("WARMING: Must be provided enough argument!\n")

        threshold = sys.argv[2]
        op.remove_empty_rows_with_threshold(data, threshold)
    #5
    elif (function == 'remove_empty_cols'):
        print('---------Remove empty columns---------')
        if len(sys.argv) < 3:
            print("To run: `python main.py remove_empty_cols threshold`")
            print("WARMING: Must be provided enough argument!\n")

        threshold = sys.argv[2]
        op.remove_empty_cols_with_threshold(data, threshold)
    #6
    elif (function == 'remove_duplicate'):
        print('---------Remove_duplicate---------')
        op.removeDuplicate(data)
    #7
    elif (function == 'norminalize'):
        print('---------Norminalize---------')
        if len(sys.argv) < 3:
            print("To run: `python main.py norminalize method`")
            print("WARMING: Must be provided enough argument!\n")

        method = sys.argv[2]
        op.norminalize(data,method)
    else:
        print("Unexpected function !!")

