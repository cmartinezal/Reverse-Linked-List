from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_nodes(self):
        node = self.head
        while node:
            sep = ',' if node.next else ''
            val = node.val if node.val else ''
            print(val, end=sep)
            node = node.next
    
    #Iterative approach
    def reverse_iterative(self, head: Node) -> Node:
        if not head:
            return head
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    #Recursive approach
    def reverse_recursive(self, head: Node, prev: Node = None) -> Node:
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_recursive(next, head)