from collections import deque

def reverse_polish_notation(str):
    stack = deque()
    postfix = ''
    operators = {'+': 0,'-': 0,'*': 2,'/': 2,'(': 3,')': 3}

    #Make
    for i in str:
        #print(i)
        #Number
        if i not in operators:
            postfix += i
        elif i == ')':
            postfix += ' '
            temp = stack.pop()
            while temp != '(':
                postfix += temp
                temp = stack.pop()
        else:
            postfix += ' '
            while len(stack) > 0:
                prev = stack.pop()
                #print('prev = ', prev)
                if prev == '(':
                    stack.append(prev)
                    stack.append(i)
                    break
                elif operators[i] <= operators[prev]:
                    #postfix += ' '
                    postfix += prev
                else:
                    stack.append(prev)
                    stack.append(i)
                    break
            else:
                stack.append(i)
        #print('string = ', postfix)

    while len(stack) > 0:
        postfix += stack.pop()

    print('postfix = ', postfix)

    #Cal
    i = 0
    while i < len(postfix):
        #print('outter while i = ', i)
        #operators
        if postfix[i] in operators:
            #print('op = ', postfix[i])
            if(len(stack)<2):
                print("Missing operan")
                return None

            b = stack.pop()
            a = stack.pop()

            #print('a = ', a)
            #print('b = ', b)

            if postfix[i] == '+':
                #print('val = ', float(a)+float(b))
                stack.append(float(a)+float(b))
            elif postfix[i] == '-':
                #print('val = ', float(a)-float(b))
                stack.append(float(a)-float(b))
            elif postfix[i] == '*':
                #print('val = ', float(a)*float(b))
                stack.append(float(a)*float(b))
            elif postfix[i] == '/':
                if float(b) == 0:
                    print("ERROR: Divided by zero")
                    return None
                #print('val = ', float(a)/float(b))
                stack.append(float(a)/float(b))
        elif (postfix[i] != ' '):
            #print('---------------while---------------')
            number = ''
            while postfix[i] != ' ' and postfix[i] not in operators:
                #print('while i = ', i)
                #print('char = ', postfix[i])
                number += postfix[i]
                i += 1
                if i >= len(postfix):
                    break
            i -= 1
            #print('number = ', number)
            stack.append(float(number))

        i += 1

    return stack.pop()
