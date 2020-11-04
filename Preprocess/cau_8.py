import csv
import operation as op


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments. Argument List:', str(sys.argv))

    if len(sys.argv) < 3:
        print("To run: `python cau_8.py expression_func expression result_name`")
        print("WARMING: Must be provided function and appropriate argument!\n")

    # reading the CSV file 
    data = op.read('data.csv')
    
    function = sys.argv[1]

    #8
    if (function == 'expression_func'):
        print('---------Expression---------')
        if len(sys.argv) < 3:
            print("To run: `python cau_8.py expression_func expression result_name`")
            print("WARMING: Must be provided enough argument!\n")

        expression = sys.argv[2]
        result_name = sys.argv[3]
        op.expression(data, expression, result_name)
