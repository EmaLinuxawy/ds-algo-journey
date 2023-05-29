class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(parentheses):
    # Create a new stack
    stack = Stack()

    # Iterate over each character in the string
    for p in parentheses:
        # If the character is an opening parenthesis, 
        # push it onto the stack
        if p == '(':
            stack.push(p)
        # If the character is a closing parenthesis, 
        # pop the top element off the stack
        # and check if it matches the opening parenthesis
        elif p == ')':
            # If the stack is empty or the top element 
            # is not an opening parenthesis,
            # the parentheses are not balanced
            if stack.is_empty() or stack.pop() != '(':
                return False

    # If the stack is empty, the parentheses are balanced
    return stack.is_empty()

balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print( is_balanced_parentheses(balanced_parentheses) )

print( is_balanced_parentheses(unbalanced_parentheses) )



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""