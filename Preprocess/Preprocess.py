import csv
import operation as op


def main():
    # reading the CSV file 
    data = op.read('data.csv')
    
    #1
    list = []
    list = op.missing_data_attribute(data)
    print('Missing attribute: ')
    print(list)


    #2
    f = op.count_missing_row(data)
    print('Count missing row: ')
    print('total rows: ', f[0], ' missing rows: ', f[1])


    #3
    op.fill_empty_value(data)



#Run
main()

#There is a problem when writting csv. Run the code below

#header = ['id', 'name', 'address', 'zip']
#rows = [
    #[1, 'Hannah', '4891 Blackwell Street, Anchorage, Alaska', 99503 ],
    #[2, 'Walton', '4223 Half and Half Drive, Lemoore, California', 97401 ],
    #[3, 'Sam', '3952 Little Street, Akron, Ohio', 93704],
    #[4, 'Chris', '3192 Flinderation Road, Arlington Heights, Illinois', 62677],
    #[5, 'Doug', '3236 Walkers Ridge Way, Burr Ridge', 61257],
#]

#with open('customers.csv', 'wt') as f:
    #csv_writer = csv.writer(f)

    #csv_writer.writerow(header) # write header

    #for row in rows:
        #csv_writer.writerow(row)


#data = op.read('data.csv')
#val = op.find_fill_value(data,'LotFrontage')
#print(val)


#if op.is_number(a):
    #print('number')
#else:
    #print('char')
