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
        self.num_nodes = 0
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
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.is_empty():
            return 0
        return self.num_nodes
        
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        self.num_nodes += 1
        temp_node = Node(item)
        is_temp_new_tail = False
        
        if self.head is None:
            self.head = temp_node
            if self.tail is None:
                self.tail = temp_node
        if not is_temp_new_tail:
            self.tail.next = temp_node
            self.tail = temp_node
            
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        self.num_nodes += 1
        temp_node = Node(item)
        is_temp_new_head = False
        
        if self.head is None:
            self.head = temp_node
            is_temp_new_head = True
            if self.tail is None:
                self.tail = temp_node
            
        if not is_temp_new_head:
            temp_node.next = self.head
            self.head = temp_node
            
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node = self.head
        
        while node != None:
            if quality(node.data) == True:
                #results.append(node_id)
                return node.data
            node = node.next
        return None
    
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        print(self.length())
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))
            
        node = self.head
        next_node = self.head.next
        found_item = False

        if self.head.data == item:
            self.head = self.head.next
            found_item = True
            if self.length() == 0:
                self.tail = None
        while next_node is not None:
            
            if next_node.data == item:
                node.next = next_node.next
                found_item = True
                if next_node == self.tail:
                    self.tail = node
                    break
                break

                
            node = next_node
            next_node = next_node.next

            print("head: {}".format(self.head))
            print("tail: {}".format(self.tail))
        if found_item:
            self.num_nodes -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

                
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
    
    #print(ll.find(lambda item: item == 'B'))

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