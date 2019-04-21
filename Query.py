import collections
from nltk.tokenize import word_tokenize
import MatrixOperations

precedence = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0, ')': 0}


class Query:

    def __init__(self, query_file):
        with open(query_file, 'r') as file:
            self.content = file.readline()

    def shunting_yard(self):
        # define precedences
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0, ')': 0}
        # declare data strucures
        output = []
        operator_stack = []
        # while there are tokens to be read
        for token in word_tokenize(self.content):
            # if left bracket
            if (token == '('):
                operator_stack.append(token)
            # if right bracket, pop all operators from operator stack onto output until we hit left bracket
            elif (token == ')'):
                operator = operator_stack.pop()
                while operator != '(':
                    output.append(operator)
                    operator = operator_stack.pop()
            # if opertor, pop operators from operator stack to queue if they are of higher precedence
            elif (token in precedence):
                # if operator stack is not empty
                if (operator_stack):
                    current_operator = operator_stack[-1]
                    while (operator_stack and precedence[current_operator] > precedence[token]):
                        output.append(operator_stack.pop())
                        if (operator_stack):
                            current_operator = operator_stack[-1]
                operator_stack.append(token)  # add token to stack
            # else if operands, add to output list
            else:
                output.append(token.lower())
        # while there are still operators on the stack, pop them into the queue
        while (operator_stack):
            output.append(operator_stack.pop())
        print('postfix:', output)  # check
        return output

    def process_query(self, dictionary):
        result_deque = collections.deque()
        parse_deque = collections.deque()
        words = self.shunting_yard()
        for token in words:
            if token not in ['AND', 'NOT', 'OR']:
                parse_deque.append(dictionary[token])
                print(type(dictionary[token]))
            elif token in ['AND', 'NOT', 'OR']:
                parse_deque.append(token)

        for token in parse_deque:
            if token not in ['AND', 'NOT', 'OR']:
                result_deque.append(token)
            elif token == 'AND':
                first = result_deque.pop()
                second = result_deque.pop()
                result_deque.append(MatrixOperations.my_and(first, second))
            elif token == 'OR':
                first = result_deque.pop()
                second = result_deque.pop()
                result_deque.append(MatrixOperations.my_or(first, second))
            elif token == 'NOT':
                first = result_deque.pop()
                result_deque.append(MatrixOperations.my_not(first))
        return result_deque



if __name__ == '__main__':
    query = Query('query.txt')
    query.shunting_yard()
