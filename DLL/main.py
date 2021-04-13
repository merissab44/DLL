from DoublyLinkedList import DoublyLinkedList

# Example:  12 ↔️ 200 ↔️ 19 ↔️ 49

dll = DoublyLinkedList()

dll.append(10)
dll.append(12)
dll.append(18)
dll.append(17)
dll.append(23)
print(dll.print_nodes())
dll.insert(13, 4)
print('ive inserted 13 at index 3')
print(dll.print_nodes())
print(dll.update(12, 16))
dll.remove(23)
print(dll.print_nodes())
dll.find(17)
