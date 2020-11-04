import csv
import math
import RPN


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

#1
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

#2
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
                break
    return [total,count]

#3
def find_fill_value(data,attribute,method):
    size = len(data)
    categorical = {}

    numeric_list = []
    sum = 0
    count = 0
    numeric_flag = False

    for row in range(1,size):
        if is_number(data[row][attribute]):
            numeric_flag = True
            if method == 'mean' or method == 'all':
                sum += float(data[row][attribute])
                count += 1

            elif method == 'median':
                numeric_list.append(float(data[row][attribute]))
            else:
                print('Unexpected method for numeric attribute')
                return ''


        elif (data[row][attribute] != ''):
            if method != 'mode':
                print('Unexpected method for categorical attribute')
                return ''
            key = data[row][attribute]
            if key not in categorical:
                categorical[key] = 0

            categorical[key] += 1
                

    if numeric_flag and (method == 'mean' or method == 'all'):
        print('Attribute: ', attribute)
        print('Mean = ', sum / count)
        return sum / count
    elif numeric_flag and method == 'median':
        #Ascending
        numeric_list.sort()
        length = len(numeric_list)
        if length % 2 == 0:
            print('Attribute: ', attribute)
            print('> Median = ', (numeric_list[length//2] + numeric_list[length//2 - 1])/2)
            return (numeric_list[length//2] + numeric_list[length//2 - 1])/2
        else:
            print('Attribute: ', attribute)
            print('> Median = ',numeric_list[length//2])
            return numeric_list[length//2]
    else:
        sort_category = sorted(categorical.items(), key=lambda item: item[1], reverse=True)
        #print(sort_category)
        if (len(sort_category) == 0):
            return ''
        print('Attribute: ', attribute)
        print('> Mode = ', sort_category[0][0])
        return sort_category[0][0]


def fill_empty_value(data,attribute = 'all',method = 'all'):
    header = data[0]
    size = len(data)
    fill_value = ''

    #Check valid
    if attribute != 'all' and attribute not in header:
        print('There is no attribute name: ', attribute)
        return None

    #Default fill numeric by mean, categorical by mode
    if (attribute == 'all'):
        for attribute in header:
            fill_value = find_fill_value(data,attribute,method)
            for row in range(1,size):
                if data[row][attribute] == '':
                    data[row][attribute] = fill_value
    #Fill attribute with appropriate method
    else:
        fill_value = find_fill_value(data,attribute,method)
        for row in range(1,size):
            if data[row][attribute] == '':
                data[row][attribute] = fill_value

    write('write.csv',data)


# cau 4
def remove_row(data, instance):
    data.remove(instance)


def remove_empty_rows_with_threshold(data, threshold):
    header = data[0]
    realData = data[1:]
    size = len(header)
    remove_list = []

    for instance in realData:
        emptyCount = 0

        for attribute in header:
            if instance[attribute] == '':
                emptyCount += 1

        if (emptyCount / size) <= (threshold / 100):
            continue

        # add instance to remove list
        remove_list.append(instance)

        
    # remove instances
    for instance in remove_list:
        remove_row(data, instance)

    write('removeRow.csv', data)


#cau 5
def remove_col(data, attribute):
    data[0].remove(attribute)

    for index in range(1, len(data)):
        data[index].pop(attribute)


def remove_empty_cols_with_threshold(data, threshold):
    header = data[0]
    realData = data[1:]
    size = len(realData)
    remove_list = []

    for attribute in header:
        emptyCount = 0

        for instance in realData:
            if instance[attribute] == '':
                emptyCount += 1

        print(attribute, emptyCount, size)

        if (emptyCount / size) <= (threshold / 100):
            continue

        # add attribute to remove list
        remove_list.append(attribute)

        
    # remove attribute
    for attribute in remove_list:
        remove_col(data, attribute)

    write('removeCol.csv', data)


# 6

def removeDuplicate(data):
    i = 1
  
    while i < len(data) - 1:
        j = i + 1

        # remove duplicate after data[i]
        while j < len(data):
            if data[i] == data[j]:
                data.pop(j)
            j += 1

        i += 1

    # write csv
    write("removeDuplicate.csv", data)


# 7
def is_numeric_attribute(data, attribute):
    for instance in data:
        if instance[attribute] != '':
            return is_number(instance[attribute])

    return False

def minmax(data, attribute):
    min_value = None
    max_value = None

    # find min and max
    for instance in data:
        if instance[attribute] == '':
            continue

        number = float(instance[attribute])
        # find min
        if min_value == None or number < min_value:
            min_value = number
        # find max
        if max_value == None or number > max_value:
            max_value = number


    # if max = min
    if max_value == min_value:
        for instance in data:
            if instance[attribute] == '':
                continue

            instance[attribute] = 0
            return 

    # update value
    for instance in data:
        if instance[attribute] == '':
            continue

        instance[attribute] = (float(instance[attribute]) - min_value) / (max_value - min_value)


def zscore(data, attribute):
    mean = 0
    stdDev = 0
    n = 0

    # calculate mean and n
    for instance in data:
        if instance[attribute] == '':
            continue

        mean += float(instance[attribute])
        n += 1
    mean /= n

    # calculate standard deviation
    for instance in data:
        if instance[attribute] == '':
            continue

        stdDev += (mean - float(instance[attribute])) ** 2
    stdDev = math.sqrt(stdDev / (n - 1))

    if (stdDev == 0):
        return
    
    # update value
    for instance in data:
        if instance[attribute] == '':
            continue

        instance[attribute] = (float(instance[attribute]) - mean) / stdDev


def norminalize(data, method):
    numeric_attr = []
    header = data[0]
    readData = data[1:]
    
    # find numeric attributes
    for attribute in header:
        if is_numeric_attribute(readData, attribute):
            numeric_attr.append(attribute)
           
    if method == "minmax":
        for attribute in numeric_attr:
            minmax(readData, attribute)
    elif method == "zscore":
        for attribute in numeric_attr:
            zscore(readData, attribute)

    write("normalize.csv", data)

    
# 8
def expression(data, expression, result_name):
    result = 0
    header = data[0]
    #Add new attribute to header
    data[0].append(result_name)
    size = len(data)
    #Check valid
    sep = [',','+','-','*','/','(',')',' ']
    default = sep[0]
    attributeList = expression
    for element in sep[1:]:
        attributeList = attributeList.replace(element,default)
    attributeList = attributeList.split(default)
    for a in attributeList:
        if a == '':
            continue
        if a not in header:
            print('Invalid input: ', a, ' does not exist in dataset')
            return -1
    #For each rows
    for row in range(1,size):
        #Replace var with value  ex: (x + y)/z -> (2 + 3)/5
        new_expression = expression
        for attribute in attributeList:
            if attribute == '':
                continue
            #Missing data or not numeric attribute
            if (data[row][attribute] == '' or is_number(data[row][attribute]) == False):
                break
            #print('data[row][attribute] = ', data[row][attribute])
            new_expression = new_expression.replace(attribute,data[row][attribute])
        #Calculate..
        result = RPN.reverse_polish_notation(new_expression)
        data[row][result_name] = str(result)

    write('write.csv',data)
    return 0
        