from stack_and_queue.stack import Stack

# https://www.youtube.com/watch?v=PLvD3pHaWHQ
# https://www.youtube.com/watch?v=TC7apM-xGaU
def is_match(paran1,paran2):
    if paran1 == "(" and paran2 ==")":
        return True
    elif paran1 == "{" and paran2 == "}":
        return True
    elif paran1 == "[" and paran2 == "]":
        return True
    else:
        return False


def is_par_balanced(baren_string):
    stack=Stack()
    is_balanced=True
    index=0

    while index < len(baren_string) and is_balanced:
        paren= baren_string[index]
        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced=False
            else:
                top=stack.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index +=1
    
    if stack.is_empty() and is_balanced:
        return True
    else:
        return False


# print(is_par_balanced(")"))