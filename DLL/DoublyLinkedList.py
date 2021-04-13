from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.length = 0

    # TODO: append()
    # Add to the end of the linked list
    def append(self, new_data):
        length = self.length
        if self.head is None:  # empty linked list
            new_node = Node(new_data)
            self.head = new_node
            self.current_node = new_node
        else:
            # create a new node
            new_node = Node(new_data)
            # set new node previousious to tail
            new_node.previous = self.current_node
            # set tail.next to new node
            self.current_node.next = new_node
            # move tail to new node
            self.current_node = new_node
        length += 1

    def print_nodes(self):
        # set the current node to the head
        current_node = self.head
        while current_node != None:
            print(f"{current_node.data} -> ", end='')
            current_node = current_node.next

    # TODO: insert()

    def insert(self, item, index):
        current = self.head
        length = self.length
        new_node = Node(item)
        inserted = False
        while inserted == False:
            if index == 0:
                self.head = new_node
                current.previous = new_node
                new_node.next = current
                inserted = True
            elif index == length:  # if we want to set as last node
                current.previous = new_node
                current.previous.next = new_node
                new_node.previous = current.previous
                new_node.next = current
                inserted = True
            else:
                current_index = 0
                while current_index != index:
                    current = current.next
                    current_index += 1
                current_index = current
                current.previous.next = new_node
                new_node.previous = current.previous
                new_node.next = current_index
                current_index.previous = new_node
                inserted = True
        length += 1

    # TODO: remove()
    def remove(self, value):
        current_node = self.head
        node_deleted = False
        # if current_node is None:
        #     node_deleted = False

        if current_node.data == value:
            # This removes it if it's the first node
            if current_node.previous == None:
                self.head = current_node.next
                self.head.previous = None
                node_deleted = True
        else:
            while current_node != None:
                if current_node.next == None:
                    current_node.previous.next = None
                    node_deleted = True
                elif current_node.data == value:  # This is if I want to delete a node in the middle of two other nodes
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    node_deleted = True
                current_node = current_node.next

        if node_deleted:  # decrease the size of the list if we deleted a node
            self.length -= 1

    # TODO: update()
    # Find and existing node with data == item and update with new value
    # traverse to find node
    # replace the data with value
    # hint: look at find() for singly linked list

    def update(self, item, value):
        current = self.head
        while current != None:
            # if we find the item to be updated, set it to the new value
            if current.data == item:
                current.data = value
            # if we didn't find it, increase the index and move to the next node
            current = current.next

    # TODO: find()
    def find(self, item):
        current_item = self.head
        index = 0
        found = False
        while current_item != None:
            # if we find the node, return it's index
            if current_item.data == item:
                found = True
                break
            # if we didn't find it, increase the index and move to the next node
            index += 1
            current_item = current_item.next
        if found:
            print(
                f'The node {current_item} is in the list at position: {index}')
