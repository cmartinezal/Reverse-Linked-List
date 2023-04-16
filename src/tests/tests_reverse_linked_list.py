import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from linked_list.linked_list import Node, LinkedList
   
def test_case_1():
    #Iterative
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    list = LinkedList()
    list.head = head
    print(f'Input = [', end="")
    list.print_nodes()
    print(']')
    output = list.reverse_iterative(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Iterative Output = [', end="")
    reversed_list.print_nodes()
    print(']')
    #Recursive
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    list = LinkedList()
    list.head = head
    output = list.reverse_recursive(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Recursive Output = [', end="")
    reversed_list.print_nodes()
    print(']')

def test_case_2():
    #Iterative
    head = Node(1)
    head.next = Node(2)
    list = LinkedList()
    list.head = head
    print(f'Input = [', end="")
    list.print_nodes()
    print(']')
    output = list.reverse_iterative(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Iterative Output = [', end="")
    reversed_list.print_nodes()
    print(']')
    #Recursive
    head = Node(1)
    head.next = Node(2)
    output = list.reverse_recursive(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Recursive Output = [', end="")
    reversed_list.print_nodes()
    print(']')

def test_case_3():
    #Iterative
    head = Node(None)
    list = LinkedList()
    list.head = head
    print(f'Input = [', end="")
    list.print_nodes()
    print(']')
    output = list.reverse_iterative(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Iterative Output = [', end="")
    reversed_list.print_nodes()
    print(']')
    #Recursive
    head = Node(None)
    output = list.reverse_recursive(head)
    reversed_list = LinkedList()
    reversed_list.head = output
    print(f'Recursive Output = [', end="")
    reversed_list.print_nodes()
    print(']')

def run_tests():
    test_case_1()
    test_case_2()
    test_case_3()
