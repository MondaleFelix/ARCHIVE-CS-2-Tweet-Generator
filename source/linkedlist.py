#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""

        # O(1), it will only take one constant step regardless of input size
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""

        # Best case: O(n)
        # Worst case: O(n) If it iterates the the entire linked list

        counter = 0 
        current_node = self.head

        while current_node is not None:
            counter +=1
            current_node = current_node.next
        return counter

        # TODO: Loop through all nodes and count one for each

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        # O(1) It will take one constant step, independent of input size

        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node





    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item


        # O(1) It will take one constant step regardless of input size 
        new_node = Node(item)

        # TODO: Prepend node before head, if it exists

        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head

        # Assigns the new node the head
        self.head = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head

        # Best case: O(1) if item was found in first node
        # Worst case: O(n) if item was found in last node

        # Checks each node and return the data (if found)
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next




    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item

        # O(n) as it has to iterate the entire linkedlist 
        
        previous_node = None
        current_node = self.head

        print(self.__repr__)


        # Checks to see if linkedlist is empty
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        if current_node is self.head:
            if self.tail  is self.head:
                self.tail = None
            self.head = current_node.next
            return

        if current_node is self.tail:
            self.tail = previous_node

            if previous_node:
                previous_node.next = None
            return



        # iterates through nodes and checks if item is data
        while item is not current_node.data:
            #
            if current_node.next is None:
                raise ValueError('Item not found: {}'.format(item))

            previous_node = current_node
            current_node = current_node.next

        # Reassigns the pointer of the previous node to the next node
        if current_node is not self.head and current_node is not self.tail:
            previous_node.next = current_node.next


        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
