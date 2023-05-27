class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
            
            self.head = first_node.next
            prev = first_node
        self.head = dummy.next
        if self.head:
            self.head.prev = None


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)

print('dll before swap_pairs:')
dll.print_list()

dll.swap_pairs() 


print('dll after swap_pairs:')
dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    dll before swap_pairs:
    1
    2
    3
    4
    dll after swap_pairs:
    2
    1
    4
    3

"""
