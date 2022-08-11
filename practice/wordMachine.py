def wordMachine(S):
    list_S = S.split(" ")
    list_stack = []
    for i in list_S:
        if i.isnumeric():
            if 0 < int(i) < 2 ** 20 - 1:
                list_stack.append(int(i))
            else:
                return -1
        elif i == 'POP':
            if len(list_stack) > 0:
                list_stack.pop()
            else:
                return -1
        elif i == 'DUP':
            if len(list_stack) > 0:
                list_stack.append(list_stack[-1])
            else:
                return -1
        elif i == '+':
            if len(list_stack) > 1:
                num_add = list_stack[-1] + list_stack[-2]
                list_stack.pop()
                list_stack.pop()
                list_stack.append(num_add)
            else:
                return -1
        elif i == '-':
            if len(list_stack) > 1:
                num_sub = list_stack[-1] - list_stack[-2]
                list_stack.pop()
                list_stack.pop()
                list_stack.append(num_sub)
            else:
                return -1
        else:
            return -1

    if len(list_stack) != 0:
        return list_stack[-1]
    else:
        return -1

s = '4 5 6 - 7 +'
print(wordMachine(s))

# t = '4'
# print(isinstance(int(t), int))