from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator
import re

PRECEDENCE = {'*': 2, '/': 2, '+': 1, '-': 1}


def tree_builder(raw_string):
    regex = r'(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])'
    string_input_list = re.findall(regex, raw_string)
    input_list = []
    for string_element in string_input_list:
        try:
            input_list.append(float(string_element))
        except ValueError:
            input_list.append(string_element)
    parent_stack = Stack()
    tree = BinaryTree('root')
    parent_stack.push(tree)
    current_tree = tree
    for token in input_list:
        if token == '(':
            current_tree.insertLeft('')
            parent_stack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif type(token) == float:
            if parent_stack and parent_stack[-1].getRootVal() == 'root':
                current_tree.insertLeft(token)
            else:
                if input_list.index(token) != 0 and input_list.index(token) != len(input_list) - 1\
                        and input_list[input_list.index(token) + 1] in ['+', '-', '*', '/'] \
                        and input_list[input_list.index(token) - 1] in ['+', '-', '*', '/']:
                    if PRECEDENCE[input_list[input_list.index(token) + 1]] > PRECEDENCE[input_list[input_list.index(token) - 1]]:
                        current_tree.insertLeft('')
                        parent_stack.push(current_tree)
                        current_tree = current_tree.getLeftChild()
                current_tree.setRootVal(token)
                parent = parent_stack.pop()
                current_tree = parent
                if input_list.index(token) >= 4\
                        and input_list[input_list.index(token) - 1] in ['+', '-', '*', '/'] \
                        and input_list[input_list.index(token) - 3] in ['+', '-', '*', '/']:
                    if PRECEDENCE[input_list[input_list.index(token) - 1]] > PRECEDENCE[input_list[input_list.index(token) - 3]]:
                        current_tree = parent_stack.pop()
        elif token in ['+', '-', '*', '/']:
            if current_tree.getRootVal() in ['+', '-', '*', '/']:
                parent_tree = BinaryTree(token)
                parent_tree.insertLeft(current_tree)
                parent_tree.insertRight('')
                parent_stack.push(parent_tree)
                current_tree = parent_tree.getRightChild()
            else:
                current_tree.setRootVal(token)
                current_tree.insertRight('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getRightChild()
        elif token == ')':
            current_tree = parent_stack.pop()
        else:
            raise ValueError
    return current_tree


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
    expression = '9*(3+5)-8/4'
    print(evaluate(tree_builder(expression)))

main()