class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev

# Sử dụng Doubly Linked List
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(1)
doubly_linked_list.insert(2)
doubly_linked_list.insert(3)

print("Forward traversal:")
doubly_linked_list.display_forward()  # Kết quả: 1 2 3

print("\nBackward traversal:")
doubly_linked_list.display_backward()  # Kết quả: 3 2 1