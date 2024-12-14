class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node 
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node 

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  

    def delete(self, data):
        current = self.head
        if current is None:  
            print("List is empty.")
            return

        if current.data == data:
            self.head = current.next 
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        
        if current is None:  
            print(f"Node with data {data} not found.")
            return

        prev.next = current.next
        current = None  

    def bubble_sort(self):
        if self.head is None:
            return

        end = None
        while end != self.head: 
            current = self.head
            while current.next != end:
                if current.data > current.next.data:  
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            end = current

    def display(self):
        current = self.head
        if not current:  
            print("The list is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 

    def quick_sort(self):
        self.head = self._quick_sort_rec(self.head)

    def _quick_sort_rec(self, head):
        if not head or not head.next:
            return head

        pivot = head
        left, right = self._partition(head, pivot)

        left = self._quick_sort_rec(left)
        right = self._quick_sort_rec(right)

        if left:
            current = left
            while current.next:
                current = current.next
            current.next = pivot
            pivot.next = right
            return left
        else:
            pivot.next = right
            return pivot

    def _partition(self, head, pivot):
        left_dummy = Node(None)
        right_dummy = Node(None)
        left = left_dummy
        right = right_dummy
        current = head.next

        while current:
            if current.data < pivot.data:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next

        left.next = None 
        right.next = None 
        pivot.next = None
        return left_dummy.next, right_dummy.next

if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.append(20)
    linked_list.append(10)
    linked_list.append(8)
    linked_list.append(52)

    print("Original List:")
    linked_list.display()

    linked_list.quick_sort()

    print("Sorted List (Quick Sort):")
    linked_list.display()
