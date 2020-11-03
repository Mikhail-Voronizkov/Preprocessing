import csv


def is_number(str):
    flag = False
    for character in str:
        if ((character < '0' or character > '9') and character != '.'):
            return False
        flag = True
    return flag


def read(filename):
    content = []
    # opening the CSV file 
    with open(filename, mode ='r')as file:
        # reading the CSV file 
        data = csv.DictReader(file)
        
        header = data.fieldnames
        content.append(header)
        for row in data:
            content.append(row)
    return content


def write(filename,data):
    header = data[0]
    rows = list(data[1:])
    with open(filename, 'wt') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(header) # write header

        for row in rows:
            csv_writer.writerow(row.values())


def missing_data_attribute(data):
    
    missing = []
    # reading the CSV file 
    #data = read('data.csv')
    header = data[0]
    size = len(data)
    # check 
    for row in range(1,size):
        #print(data[row]['Alley'])
        for attribute in header:
            if (data[row][attribute] == '' and attribute not in missing):
                missing.append(attribute)
    return missing


def count_missing_row(data):
    count = 0
    total = 0
    # reading the CSV file 
    #data = read('data.csv')
    header = data[0]
    size = len(data)
    # counting
    for row in range(1,size):
        total += 1
        for attribute in header:
            if (data[row][attribute] == ''):
                count+= 1
                break;
    return [total,count]


def find_fill_value(data,attribute):
    size = len(data)
    categorical = {}

    sum = 0
    count = 0
    numeric_flag = False

    for row in range(1,size):
        if is_number(data[row][attribute]):
            #print(data[row][attribute])
            sum += float(data[row][attribute])
            count += 1
            numeric_flag = True
        elif (data[row][attribute] != ''):
            key = data[row][attribute]
            if key not in categorical:
                categorical[key] = 0

            categorical[key] += 1
                

    if numeric_flag:
        return sum / count
    else:
        sort_category = sorted(categorical.items(), key=lambda item: item[1], reverse=True)
        print(sort_category)
        if (len(sort_category) == 0):
            return ''
        return sort_category[0][0]


def fill_empty_value(data):
    header = data[0]
    size = len(data)
    fill_value = ''
   
    for attribute in header:
        fill_value = find_fill_value(data,attribute)
        for row in range(1,size):
            if data[row][attribute] == '':
                data[row][attribute] = fill_value

    write('write.csv',data)
    

    
        