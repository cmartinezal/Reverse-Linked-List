class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def display(self):
        while self:
            sep = ',' if self.next else ''
            val = self.val if self.val else ''
            print(val, end=sep)
            self = self.next

class Solution:
    #Iterative approach
    def reverse_linked_list(self, head: Node) -> Node:
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
    def reverse_linked_list2(self, head: Node, prev: Node = None) -> Node:
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_linked_list2(next, head)

#Tests
sol = Solution()

#Case 1
#Iterative
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(f'Input = [', end="")
head.display()
print(']')
output = sol.reverse_linked_list(head)
print(f'Iterative Output = [', end="")
output.display()
print(']')
#Recursive
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
output = sol.reverse_linked_list2(head)
print(f'Recursive Output = [', end="")
output.display()
print(']')

#Case 2
#Iterative
head = Node(1)
head.next = Node(2)
print(f'Input = [', end="")
head.display()
print(']')
output = sol.reverse_linked_list(head)
print(f'Iterative Output = [', end="")
output.display()
print(']')
#Recursive
head = Node(1)
head.next = Node(2)
output = sol.reverse_linked_list2(head)
print(f'Recursive Output = [', end="")
output.display()
print(']')

#Case 3
#Iterative
head = Node(None)
print(f'Input = [', end="")
head.display()
print(']')
output = sol.reverse_linked_list(head)
print(f'Iterative Output = [', end="")
output.display()
print(']')
#Recursive
head = Node(None)
output = sol.reverse_linked_list2(head)
print(f'Recursive Output = [', end="")
output.display()
print(']')