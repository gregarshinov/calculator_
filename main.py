from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

PRECEDENCE = {'*': 2, '/': 2, '+': 1, '-': 1}


def tree_builder(raw_string):
    string_input_list = raw_string.split()
    input_list = []
    for string_element in string_input_list:
        try:
            input_list.append(float(string_element))
        except ValueError:
            input_list.append(string_element)
    parent_stack = Stack()
    tree = BinaryTree('')
    parent_stack.push(tree)
    current_tree = tree
    for token in input_list:
        if token == '(':
            current_tree.insertLeft('')
            parent_stack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif type(token) == float:
            current_tree.setRootVal(token)
            parent = parent_stack.pop()
            current_tree = parent
        elif token in ['+', '-', '*', '/']:
            current_tree.setRootVal(token)
            current_tree.insertRight('')
            parent_stack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif token == ')':
            current_tree = parent_stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(expression_tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = expression_tree.getLeftChild()
    right_child = expression_tree.getRightChild()

    if left_child and right_child:
        operation = operators[expression_tree.getRootVal()]
        return operation(evaluate(left_child), evaluate(right_child))
    else:
        return expression_tree.getRootVal()




def main():
    expression = '9 + ( 3 + 5 ) - 8 '
    print(evaluate(tree_builder(expression)))

main()
