# Discussion questions

# 1. Given the linked list below, which are the nodes? What is the data for each
#    node? Where is the head? Where is the tail? (Please be as specific as
#    possible — exactly which parts of the diagram correspond to each part?
#    Arrows? Boxes? Text?)
#       Apple (data: "Apple"), Berry (data: "Berry"), and Cherry
#       (data: "Cherry") are nodes
#       In this diagram, there is no tail.

# 2. What’s the difference between doubly- and singly-linked lists?
#       Nodes in singly-linked lists have a next attribute, while nodes in 
#       doubly-linked lists have a next and a prev attribute.

# 3. Why is it faster to append to a linked list if we keep track of the tail
#    as an attribute?
#       It's faster to append to a linked list if we add a tail attribute,
#       because that way we don't have to traverse the list every time we 
#       add a node (we know where the end is).

##########################################################################

# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """

        current = self.head

        while current is not None:
            print current.data
            current = current.next


    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>
        """

        current = self.head

        i = 1
        while i <= idx:
            current = current.next
            i += 1

        return current

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

