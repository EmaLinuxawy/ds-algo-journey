class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        return slow
    
def find_kth_from_end(head, k):
    slow = head
    fast = head
    count = 1
    while slow is not None:
        if count == k + 1:
            return None
        else:
            count += 1
    return count

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)
#print( my_linked_list.find_middle_node().value )
